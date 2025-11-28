# Sistema Bancário Simples

Um projeto em Python que implementa um sistema bancário simples para fins educacionais. Este repositório contém módulos para gerenciar clientes, contas, transações e uma interface simples (`ui.py`) para interação.

## Visão geral

Funcionalidades principais:
- Cadastro e gerenciamento de clientes
- Criação e consulta de contas bancárias
- Registros de transações (depósito, saque, transferência)
- Interface simples (linha de comando) para executar operações

O projeto foi organizado em módulos: `banco.py`, `clientes.py`, `contas.py`, `transacoes.py` e `ui.py`.

## Requisitos

- Python 3.8+
- (Opcional) virtualenv/venv para isolar o ambiente

> Não há dependências externas listadas no repositório (arquivo `requirements.txt` não incluído). Se adicionar bibliotecas, crie um `requirements.txt`.

## Instalação (local)

1. Clone o repositório:

```bash
git clone <URL-do-repositório>
cd Sistema_Bancario_Simples
```

2. (Recomendado) Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale dependências (se houver):

```bash
pip install -r requirements.txt
```

## Como executar

A forma mais simples de usar o sistema é executando a interface:

```bash
python3 ui.py
```

A `ui.py` fornece um menu/fluxo de execução para criar clientes, abrir contas, listar contas e realizar transações.

Se preferir usar os módulos diretamente (por exemplo em scripts ou REPL):

```python
from banco import Banco
# exemplo hipotético
b = Banco()
# use métodos do projeto para manipular clientes/contas
```

## Estrutura do projeto

- `banco.py` — lógica do banco (orquestra operações entre clientes, contas e transações)
- `clientes.py` — modelo e funções de gerenciamento de clientes
- `contas.py` — definição e operações sobre contas bancárias
- `transacoes.py` — lógica para depósitos, saques e transferências
- `ui.py` — interface de linha de comando para interação com o sistema
- `__init__.py` — pacote Python

## Exemplos de uso

- Criar cliente e abrir conta via `ui.py`.
- Simular depósitos e saques para testar o comportamento.

(O conteúdo exato dos exemplos pode ser complementado com trechos do código do projeto, se quiser que eu extraia e insira exemplos reais.)

## Testes

Não há tests automatizados incluídos no repositório atualmente. Sugestão:

- Adicionar testes unitários com `pytest` cobrindo operações críticas (depósito, saque, transferência e regras de saldo).
- Incluir um `requirements-dev.txt` ou `pyproject.toml` para dependências de desenvolvimento.

## Como contribuir

Contribuições são bem-vindas. Sugestões:
- Abra uma issue descrevendo o problema ou a feature.
- Crie uma branch com namespace `feature/` ou `fix/` e faça um PR com descrição e testes quando possível.

## Melhorias sugeridas

- Adicionar persistência (arquivo JSON, SQLite ou outro banco de dados).
- Implementar testes unitários e CI (GitHub Actions).
- Criar uma interface gráfica ou API REST para exposição do serviço.

## Licença

Inclua um arquivo `LICENSE` com a licença desejada (por exemplo MIT) ou adicione a seção aqui.
