"""
Projeto: Santander Dev Week 2023 - ETL com Python e IA

Objetivo:
- Extração: ler clientes de um arquivo CSV.
- Transformação: gerar uma mensagem personalizada para cada cliente.
- Carregamento: salvar o resultado em CSV e JSON.

Este projeto funciona mesmo sem a API pública da Santander Dev Week.
Se OPENAI_API_KEY estiver configurada, o script tenta usar IA generativa via OpenAI.
Se não estiver configurada, usa um gerador local de mensagens para manter o ETL executável.
"""

from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List

import pandas as pd

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "clientes.csv"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_CSV = OUTPUT_DIR / "clientes_com_mensagens.csv"
OUTPUT_JSON = OUTPUT_DIR / "clientes_com_mensagens.json"

REQUIRED_COLUMNS = ["id", "nome", "conta", "cartao", "saldo", "perfil", "objetivo"]

ICON_URL = "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg"


def extract_users(csv_path: Path = DATA_PATH) -> List[Dict]:
    """Extrai os dados de clientes a partir de um CSV."""
    if not csv_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {csv_path}")

    df = pd.read_csv(csv_path)

    missing_columns = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing_columns:
        raise ValueError(f"Colunas obrigatórias ausentes no CSV: {missing_columns}")

    return df.to_dict(orient="records")


def limit_message(message: str, max_chars: int = 100) -> str:
    """Garante que a mensagem fique dentro do limite solicitado no desafio."""
    clean_message = " ".join(str(message).replace('"', "").split())

    if len(clean_message) <= max_chars:
        return clean_message

    return clean_message[: max_chars - 3].rstrip() + "..."


def generate_local_message(user: Dict) -> str:
    """
    Gera uma mensagem personalizada sem depender de APIs externas.

    Este modo mantém o projeto executável para o desafio, mesmo sem chave de IA
    e mesmo com a API original fora do ar.
    """
    nome = user["nome"]
    perfil = str(user["perfil"]).lower()
    objetivo = str(user["objetivo"]).lower()

    if "conservador" in perfil:
        message = f"{nome}, comece com segurança: sua reserva fortalece seus próximos investimentos."
    elif "arrojado" in perfil:
        message = f"{nome}, diversifique seus investimentos e transforme estratégia em crescimento."
    elif "iniciante" in perfil:
        message = f"{nome}, organize hoje seu dinheiro e dê o primeiro passo para investir melhor."
    elif "viagem" in objetivo:
        message = f"{nome}, invista aos poucos e aproxime sua próxima viagem da realidade."
    else:
        message = f"{nome}, investir todo mês pode aproximar você dos seus objetivos financeiros."

    return limit_message(message)


def generate_openai_message(user: Dict) -> str | None:
    """
    Tenta gerar a mensagem usando a OpenAI.

    Para usar:
    1. Instale as dependências: pip install -r requirements.txt
    2. Crie um arquivo .env baseado no .env.example
    3. Configure OPENAI_API_KEY
    """
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return None

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)
        model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

        prompt = (
            "Crie uma mensagem bancária personalizada em português do Brasil, "
            "com no máximo 100 caracteres, incentivando investimentos de forma ética, "
            "sem prometer ganhos. Dados do cliente: "
            f"nome={user['nome']}, perfil={user['perfil']}, objetivo={user['objetivo']}."
        )

        response = client.responses.create(
            model=model,
            input=[
                {
                    "role": "developer",
                    "content": "Você é especialista em marketing bancário responsável e educação financeira.",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            max_output_tokens=80,
        )

        return limit_message(response.output_text)

    except Exception as error:
        print(f"Aviso: não foi possível usar OpenAI. Motivo: {error}")
        return None


def generate_ai_message(user: Dict) -> str:
    """Usa OpenAI quando disponível; caso contrário, usa o gerador local."""
    message = generate_openai_message(user)

    if message:
        return message

    return generate_local_message(user)


def transform_users(users: List[Dict]) -> List[Dict]:
    """Transforma os dados criando uma mensagem personalizada para cada cliente."""
    transformed_users = []

    for user in users:
        news_description = generate_ai_message(user)

        transformed_user = {
            **user,
            "news_icon": ICON_URL,
            "news_description": news_description,
            "processed_at": datetime.now().isoformat(timespec="seconds"),
        }

        transformed_users.append(transformed_user)

    return transformed_users


def load_users(users: List[Dict]) -> None:
    """Carrega os dados transformados em arquivos CSV e JSON."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(users)
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")

    with OUTPUT_JSON.open("w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=2)


def main() -> None:
    """Executa o pipeline ETL completo."""
    if load_dotenv:
        load_dotenv()

    print("Iniciando pipeline ETL...")

    users = extract_users()
    print(f"Extract concluído: {len(users)} clientes extraídos.")

    transformed_users = transform_users(users)
    print("Transform concluído: mensagens personalizadas geradas.")

    load_users(transformed_users)
    print(f"Load concluído: arquivo CSV salvo em {OUTPUT_CSV}")
    print(f"Load concluído: arquivo JSON salvo em {OUTPUT_JSON}")

    print("\nPrévia do resultado:")
    preview_columns = ["id", "nome", "perfil", "objetivo", "news_description"]
    print(pd.DataFrame(transformed_users)[preview_columns].to_string(index=False))


if __name__ == "__main__":
    main()
