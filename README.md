Automacao Selenium Python
Projeto de estudos em automação de testes web com Python e Selenium WebDriver.

O objetivo é construir uma base simples, organizada e evolutiva para praticar conceitos de QA, automação E2E, boas práticas de seletores, waits explícitos e estruturação de testes.

Status
Em evolução.

Objetivos
Praticar automação web com Selenium WebDriver
Organizar testes de forma legível e reutilizável
Evoluir para uso de Page Object Model
Adicionar execução com pytest
Preparar o projeto para integração futura com CI/CD
Stack
Python 3
Selenium WebDriver
Pytest, em evolução
VS Code
Git e GitHub
Estrutura sugerida
Automacao-Selenium-Python/
├── tests/
├── pages/
├── utils/
├── requirements.txt
└── README.md
Como preparar o ambiente
git clone https://github.com/Demetrios10/Automacao-Selenium-Python.git
cd Automacao-Selenium-Python
python -m venv .venv
No Windows:

.venv\Scripts\activate
No Linux/macOS:

source .venv/bin/activate
Instale as dependências iniciais:

pip install selenium pytest
Exemplo base
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
print(driver.title)
driver.quit()
Boas práticas aplicadas
Usar waits explícitos em vez de esperas fixas
Priorizar seletores estáveis
Separar páginas, testes e utilitários
Manter dados de teste fora da lógica dos testes
Escrever nomes de testes claros e objetivos
Próximos passos
Criar testes reais dentro de tests/
Adicionar Page Objects dentro de pages/
Criar requirements.txt
Adicionar execução com pytest
Adicionar workflow de CI com GitHub Actions
Autor
Demétrios Alves Da Silva
