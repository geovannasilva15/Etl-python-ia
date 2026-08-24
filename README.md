<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=f59e0b&height=180&section=header&text=ETL%20com%20Python&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=34&desc=Dados%2C%20automa%C3%A7%C3%A3o%20e%20mensagens%20personalizadas&descAlignY=57" alt="ETL com Python" />

</div>

<div align="center">

[![Python](https://img.shields.io/badge/Python-ETL-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![CSV](https://img.shields.io/badge/Entrada-CSV-16A34A?style=for-the-badge)](#)
[![JSON](https://img.shields.io/badge/Saída-CSV_e_JSON-111827?style=for-the-badge)](#)

**Pipeline educacional de ETL desenvolvido para o desafio Santander Dev Week.**

</div>

## Sobre

O projeto demonstra um fluxo completo de **extração, transformação e carregamento de dados**. Registros são lidos de uma base CSV, processados em Python para gerar mensagens personalizadas e exportados em formatos estruturados.

## Fluxo do projeto

```mermaid
flowchart LR
    A[CSV de entrada] --> B[Extração]
    B --> C[Transformação em Python]
    C --> D[Mensagens personalizadas]
    D --> E[CSV e JSON]
```

## Estrutura

O código principal está em `santander-etl-python-ia/src/main.py`, acompanhado de dados de entrada, resultados e documentação específica.

## Executar

```bash
git clone https://github.com/geovannasilva15/Etl-python-ia.git
cd Etl-python-ia/santander-etl-python-ia
pip install -r requirements.txt
python src/main.py
```

## Aprendizados

- Construção de pipeline ETL
- Leitura e transformação de arquivos CSV
- Geração de conteúdo personalizado
- Exportação de dados em CSV e JSON
- Organização modular de um projeto Python

## Autoria

Desenvolvido por **[Geovanna Eduarda da Silva](https://github.com/geovannasilva15)**.
