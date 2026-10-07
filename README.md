# Pipeline ETL com Python

Projeto desenvolvido a partir do desafio do Santander Dev Week para demonstrar um fluxo completo de extração, transformação e carregamento de dados. O pipeline processa uma base fictícia de clientes e gera mensagens de educação financeira personalizadas.

## Fluxo

```mermaid
flowchart LR
    CSV[CSV de entrada] --> EX[Extração]
    EX --> TR[Transformação em Python]
    TR --> OUT[CSV e JSON]
```

O pipeline lê registros de clientes, valida a estrutura da entrada, cria mensagens personalizadas e exporta os resultados em formatos estruturados. A execução funciona localmente sem serviços externos; o uso da API da OpenAI é opcional.

## Resultado verificado

| Verificação | Resultado |
|---|---:|
| Registros processados | 5 |
| Mensagens com até 100 caracteres | 5 de 5 |
| Formatos gerados | CSV e JSON |
| Execução sem chave externa | Sim |

## Estrutura

```text
data/       dados de entrada
notebooks/  exploração do processo
output/     resultados gerados
src/        código principal
tests/      testes automatizados
```

## Executar

```bash
python -m venv .venv
pip install -r requirements.txt
python src/main.py
```

Os arquivos processados serão gravados em `output/`.

## OpenAI opcional

Para gerar as mensagens com um modelo da OpenAI, copie `.env.example` para `.env` e informe sua chave:

```bash
OPENAI_API_KEY=sua_chave
OPENAI_MODEL=gpt-4.1-mini
```

Sem essa configuração, o pipeline usa regras locais e continua totalmente executável.

## Testes

```bash
python -m unittest discover -s tests -v
```

Os testes cobrem leitura da base, validação das colunas, limite das mensagens e geração dos arquivos finais.

## Tecnologias e práticas

`Python` `pandas` `CSV` `JSON` `ETL` `OpenAI opcional`

## Autoria

[Geovanna Eduarda da Silva](https://github.com/geovannasilva15)
