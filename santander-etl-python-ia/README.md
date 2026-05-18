# Santander Dev Week 2023 — ETL com Python e IA

Projeto desenvolvido para o desafio prático de **Ciência de Dados com Python**, com foco no fluxo **ETL**:

- **Extract:** leitura dos dados de clientes a partir de um arquivo CSV.
- **Transform:** geração de mensagens personalizadas para cada cliente.
- **Load:** gravação dos dados enriquecidos em arquivos CSV e JSON.

A API pública usada originalmente na Santander Dev Week pode estar indisponível. Por isso, este projeto usa uma abordagem local, mantendo o aprendizado principal do Lab: entender como os dados fluem de uma etapa para a outra.

---

## Tecnologias utilizadas

- Python
- Pandas
- CSV
- JSON
- OpenAI API, opcional
- Git e GitHub

---

## Estrutura do projeto

```text
santander-etl-python-ia/
├── data/
│   └── clientes.csv
├── notebooks/
│   └── Santander_ETL_Local.ipynb
├── output/
│   ├── clientes_com_mensagens.csv
│   └── clientes_com_mensagens.json
├── src/
│   └── main.py
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Dados de entrada

O arquivo `data/clientes.csv` contém dados fictícios de clientes:

| Coluna | Descrição |
|---|---|
| id | Identificador do cliente |
| nome | Nome do cliente |
| conta | Número fictício da conta |
| cartao | Cartão mascarado |
| saldo | Saldo fictício |
| perfil | Perfil financeiro |
| objetivo | Objetivo financeiro |

---

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/santander-etl-python-ia.git
cd santander-etl-python-ia
```

### 2. Crie e ative o ambiente virtual

No Windows PowerShell:

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

No Git Bash ou Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o ETL

```bash
python src/main.py
```

---

## Uso com IA generativa real

O projeto funciona sem chave da OpenAI, usando um gerador local de mensagens.

Se quiser usar IA generativa real:

1. Copie o arquivo `.env.example` para `.env`.
2. Preencha sua chave:

```text
OPENAI_API_KEY=sua_chave_aqui
```

3. Execute novamente:

```bash
python src/main.py
```

---

## Saídas geradas

Após a execução, os arquivos finais ficam na pasta `output/`:

- `clientes_com_mensagens.csv`
- `clientes_com_mensagens.json`

Exemplo de mensagem gerada:

```text
Geovanna, comece com segurança: sua reserva fortalece seus próximos investimentos.
```

---

## Explicação do ETL

### Extract

A etapa de extração lê o arquivo `clientes.csv` com a biblioteca Pandas e transforma os dados em uma lista de dicionários.

### Transform

A etapa de transformação cria uma mensagem personalizada para cada cliente, considerando nome, perfil e objetivo financeiro.

### Load

A etapa de carregamento salva os dados enriquecidos em dois formatos:

- CSV, para análise tabular.
- JSON, para simular uma estrutura parecida com retorno de API.

---

## Como publicar no GitHub

```bash
git init
git add .
git commit -m "Projeto ETL com Python e IA"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/santander-etl-python-ia.git
git push -u origin main
```

---

## Sobre o projeto

Este projeto demonstra a aplicação prática de um pipeline ETL em Python, substituindo a dependência de uma API externa por uma fonte local em CSV. A solução mantém o objetivo do desafio e mostra uma alternativa realista para cenários em que uma fonte de dados fica indisponível.
