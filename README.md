# Pipeline ETL com Python

Projeto educacional desenvolvido durante o Santander Dev Week para praticar extração, transformação e carregamento de dados.

## Fluxo

```mermaid
flowchart LR
    CSV[CSV de entrada] --> EX[Extração]
    EX --> TR[Transformação em Python]
    TR --> OUT[CSV e JSON]
```

O pipeline lê registros de clientes, aplica regras de transformação, cria mensagens personalizadas e exporta os resultados em formatos estruturados.

## Estrutura

```text
data/       dados de entrada
notebooks/  exploração do processo
output/     resultados gerados
src/        código principal
```

## Executar

```bash
python -m venv .venv
pip install -r requirements.txt
python src/main.py
```

## Tecnologias e práticas

`Python` `CSV` `JSON` `ETL` `Organização modular`

## Autoria

[Geovanna Eduarda da Silva](https://github.com/geovannasilva15)
