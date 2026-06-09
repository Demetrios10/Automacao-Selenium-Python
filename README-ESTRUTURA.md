# 🚀 Automação de Testes com Selenium + Python

## 📋 Sobre o Projeto

Projeto de automação de testes usando Selenium WebDriver e Python com Pytest, seguindo o padrão Page Object Model (POM) e BDD com Gherkin.

---

## 📁 Estrutura do Projeto

```
automação/
│
├── features/                          # Testes em formato BDD (Gherkin)
│   ├── login.feature                 # Cenários de login
│   └── steps/
│       ├── __init__.py
│       └── test_login_steps.py       # Implementação dos steps
│
├── pages/                            # Page Object Model
│   ├── __init__.py
│   ├── base_page.py                 # Classe base com métodos comuns
│   ├── home_page.py                 # Page Object da página inicial
│   └── login_page.py                # Page Object da página de login
│
├── tests/                           # Testes automatizados
│   ├── __init__.py
│   ├── test_ct01_adicionar_produtos_carrinho.py
│   ├── test_ct02_login_valido.py
│   ├── test_ct03_login_invalido.py
│   └── test_ct04_realizando_compras_1_produto.py
│
├── utils/                           # Utilitários e helpers
│   ├── __init__.py
│   └── driver_factory.py            # Factory do WebDriver e screenshot utils
│
├── reports/                         # Relatórios de testes
│   └── (gerados automaticamente)
│
├── screenshots/                     # Capturas de tela
│   └── (capturadas em caso de falhas)
│
├── conftest.py                      # Configurações do Pytest (fixtures)
├── pytest.ini                       # Configuração do Pytest
├── requirements.txt                 # Dependências do projeto
└── README.md                        # Este arquivo
```

---

## 🛠️ Pré-requisitos

- Python 3.8+
- pip
- Chrome/Chromium instalado

---

## ⚙️ Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

---

## 🧪 Executando os Testes

### Executar todos os testes
```bash
pytest
```

### Executar com mais verbosidade
```bash
pytest -v
```

### Executar arquivo específico
```bash
pytest tests/test_ct02_login_valido.py -v
```

### Executar teste específico
```bash
pytest tests/test_ct02_login_valido.py::TestLogin::test_login_valido -v
```

### Executar com marcadores
```bash
# Apenas testes de login
pytest -m login -v

# Apenas testes críticos
pytest -m critical -v
```

### Gerar relatório HTML
```bash
pytest --html=reports/report.html --self-contained-html
```

### Executar testes em paralelo
```bash
pytest -n auto
```

### Reexecutar testes que falharam
```bash
pytest --lf
```

---

## 📋 Padrões Utilizados

### Page Object Model (POM)
Cada página da aplicação tem uma classe correspondente em `pages/`. Exemplo:

```python
# pages/login_page.py
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "email")
    SENHA_INPUT = (By.ID, "senha")
    BOTAO_LOGIN = (By.ID, "btn-login")
    MENSAGEM_ERRO = (By.CLASS_NAME, "erro")
    
    def preencher_email(self, email):
        self.preencher(self.EMAIL_INPUT, email)
    
    def preencher_senha(self, senha):
        self.preencher(self.SENHA_INPUT, senha)
    
    def clicar_botao_login(self):
        self.clicar(self.BOTAO_LOGIN)
```

### BDD com Gherkin
Os cenários estão em `features/` em formato `.feature`:

```gherkin
Funcionalidade: Login
  Cenário: Login válido
    Dado que estou na página de login
    Quando preencho o email com "usuario@teste.com"
    ...
```

---

## 📦 Dependências

- **selenium**: Framework de automação web
- **pytest**: Framework de testes
- **pytest-html**: Gerador de relatórios HTML
- **pytest-xdist**: Execução paralela de testes
- **webdriver-manager**: Gerenciamento automático do ChromeDriver
- **Pillow**: Manipulação de imagens
- **python-dotenv**: Gerenciamento de variáveis de ambiente

---

## 🔧 Configuração

### conftest.py
Define fixtures reutilizáveis para todos os testes:
- `driver`: Fornece instância do WebDriver
- `driver_com_screenshot`: Captura screenshots em falhas

### pytest.ini
Configurações do Pytest como:
- Padrão de nomes de testes
- Caminho dos testes
- Marcadores customizados
- Opções de execução

---

## 💡 Exemplo de Teste

```python
# tests/test_ct02_login_valido.py
import pytest
from pages.login_page import LoginPage

class TestLogin:
    @pytest.mark.login
    def test_login_valido(self, driver):
        """Teste de login com credenciais válidas"""
        login_page = LoginPage(driver)
        login_page.abrir_pagina()
        login_page.preencher_email("usuario@teste.com")
        login_page.preencher_senha("senha123")
        login_page.clicar_botao_login()
        
        assert driver.current_url.endswith("/home")
```

---

## 📊 Gerando Relatórios

### Relatório HTML
```bash
pytest --html=reports/relatorio.html --self-contained-html -v
```

### Com screenshots de falhas
O arquivo `conftest.py` já está configurado para capturar screenshots automaticamente em caso de falhas.

---

## 🐛 Troubleshooting

### ChromeDriver não encontrado
```bash
pip install --upgrade webdriver-manager
```

### Timeouts nos testes
Ajuste o `implicitly_wait` em `conftest.py`:
```python
driver.implicitly_wait(15)  # aumentar para 15 segundos
```

### Testes falhando por elemento não encontrado
Use `WebDriverWait` e `expected_conditions` em `base_page.py`

---

## 📚 Recursos Úteis

- [Documentação Selenium](https://selenium.dev/documentation/)
- [Documentação Pytest](https://docs.pytest.org/)
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)

---

## 👨‍💻 Autor

Seu Nome - [GitHub](https://github.com/seu-usuario)

---

## 📄 Licença

Este projeto está sob a licença MIT.
