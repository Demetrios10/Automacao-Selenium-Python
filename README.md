# Automação Selenium com Python

Repositório de estudos em automação de testes web usando Python, Selenium WebDriver e boas práticas de QA.

## Visão geral

Este projeto tem como objetivo criar uma base simples e evolutiva para praticar automação E2E. A proposta é organizar testes, páginas e utilitários de forma clara, facilitando manutenção, leitura e evolução para cenários mais reais.

## Status do projeto

Em evolução.

| Item | Situação |
| --- | --- |
| Estrutura inicial | Em preparação |
| Selenium WebDriver | Em estudo |
| Pytest | Próximo passo |
| Page Object Model | Próximo passo |
| GitHub Actions | Futuro |

## Tecnologias

- Python 3
- Selenium WebDriver
- Pytest
- VS Code
- Git e GitHub

## Estrutura sugerida

```text
Automacao-Selenium-Python/
|-- tests/
|-- pages/
|-- utils/
|-- requirements.txt
`-- README.md
```

## Como preparar o ambiente

Clone o repositório:

```bash
git clone https://github.com/Demetrios10/Automacao-Selenium-Python.git
cd Automacao-Selenium-Python
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente no Windows:

```bash
.venv\Scripts\activate
```

Ative o ambiente no Linux ou macOS:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install selenium pytest
```

## Exemplo inicial

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
print(driver.title)
driver.quit()
```

## Boas práticas

- Usar waits explícitos no lugar de esperas fixas
- Priorizar seletores estáveis e fáceis de manter
- Separar testes, páginas e funções auxiliares
- Nomear testes de forma clara e objetiva
- Manter dados de teste separados da lógica dos testes

## Roadmap

- Criar os primeiros testes dentro de `tests/`
- Adicionar Page Objects dentro de `pages/`
- Criar arquivo `requirements.txt`
- Configurar execução com `pytest`
- Adicionar relatório de execução
- Criar workflow de CI com GitHub Actions

## Autor

Demétrios Alves Da Silva
