# Automação web com Selenium e Python

[Estudo de caso](docs/PORTFOLIO.md)

**QA · Selenium WebDriver · Page Object Model · unittest**

Projeto de estudo para preencher e validar o [formulário de cadastro do Automation Testing](https://demo.automationtesting.in/Register.html), com dados fictícios e sem enviar o cadastro ao servidor.

[Como executar](#como-executar) · [Testes](#testes) · [Arquitetura](#organização-do-projeto) · [Evidências](evidencias/README.md) · [Contribuir](CONTRIBUTING.md)

## Objetivo

Praticar a separação entre interação com a página, gerenciamento do navegador, fluxo de demonstração e asserções. O código utiliza esperas explícitas, sessões isoladas por cenário e encerramento do navegador ao finalizar a sessão.

## Instalação

Requer Python 3, Google Chrome e acesso à internet.

```bash
git clone https://github.com/Demetrios10/Automacao-Selenium-Python.git
cd Automacao-Selenium-Python
python -m venv .venv
```

Instale com o Python do ambiente virtual:

```powershell
# Windows / PowerShell
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

```bash
# Linux / macOS
.venv/bin/python -m pip install -r requirements.txt
```

Os comandos seguintes usam `python` com o ambiente ativado. Se preferir, substitua pelo caminho do executável do ambiente virtual mostrado acima.

## Como executar

```bash
python -m scripts.cadastro
```

A demonstração preenche dados fictícios e confere a leitura dos campos. Para execução sem janela, use `python -m scripts.cadastro --headless`. A demonstração não comprova cadastro bem-sucedido no backend.

## Testes

### Suíte padrão

```bash
python -m unittest discover -s tests -v
```

A execução padrão roda os unitários com mocks e ignora os E2E que exigem habilitação explícita. Os unitários não abrem o site nem comprovam o comportamento real do Chrome.

### Cenários reais no PowerShell

```powershell
$env:RUN_E2E = "1"
python -m unittest discover -s tests -p test_register_e2e.py -v
Remove-Item Env:RUN_E2E
```

Opcional: defina `$env:HEADLESS = "1"` antes da execução e remova a variável depois. Cada cenário usa uma sessão própria do Chrome. Mantenha as evidências de falha; não substitua os resultados reais por simulações aprovadas.

## Estado de validação

| Camada | Situação verificada em 16/11/2026 |
|---|---|
| Sem navegador | 12 aprovados: oito testes do Page Object e quatro do coletor |
| E2E na suíte padrão | 11 ignorados por exigirem `RUN_E2E=1` |
| Tentativa real | Os 11 cenários apresentaram erro ao iniciar o Chrome; a página não foi aberta |
| Cadastro no servidor | Fora do escopo; nenhum envio é realizado |

Veja a [revisão atual](evidencias/REVISAO-2026-11-16.md) e o [relatório histórico](docs/RELATORIO-TESTES.md). Os erros de inicialização não são aprovação E2E.

## Cenários definidos

Nome e sobrenome; nome obrigatório; e-mail válido/inválido; telefone de nove/dez dígitos; exclusividade de gênero; múltiplos hobbies; senhas iguais/diferentes; limpeza pelo botão Refresh.

As regras verificadas refletem o HTML e JavaScript consultados para o formulário, incluindo telefone com dez dígitos e confirmação de senha no evento blur.

## Organização do projeto

| Caminho | Responsabilidade |
|---|---|
| [pages/register_page.py](pages/register_page.py) | Seletores, ações, esperas e leitura do estado |
| [core/browser.py](core/browser.py) | Criação e encerramento do navegador |
| [core/evidencias.py](core/evidencias.py) | Pastas, erros e capturas de evidência |
| [scripts/cadastro.py](scripts/cadastro.py) | Demonstração do fluxo |
| [tests/test_register_page.py](tests/test_register_page.py) | Oito testes unitários |
| [tests/test_register_e2e.py](tests/test_register_e2e.py) | 11 cenários reais |
| [evidencias/README.md](evidencias/README.md) | Organização dos registros de execução |

As asserções ficam nos testes; o Page Object encapsula a página. O histórico do fluxo anterior de YouTube permanece nos commits, fora do código ativo.

## Limitações e evolução

O site utiliza recursos HTTP dentro de uma página HTTPS, sujeitos a bloqueio pelo navegador. Recursos dinâmicos, listas e backend externos também podem falhar. País, idiomas, habilidades, nascimento e upload ainda não fazem parte dos cenários automatizados.

O GitHub Actions executa a suíte sem navegador em pushes e pull requests. Os 11 E2E ficam em um job manual opcional, habilitado por `run_e2e`; exigem Chrome funcional e acesso ao site.

## Padrões do projeto

Veja [estrutura, responsabilidades e evidências](docs/PADROES-QA.md).

## Revisão e autoria

Última revisão registrada em [16/11/2026](evidencias/REVISAO-2026-11-16.md). O resultado de cada nova execução fica na aba **Actions**.

**Demétrios Alves da Silva** · QA Analyst · [Portfólio](https://github.com/Demetrios10/Demetrios10/blob/main/PORTFOLIO.md) · [LinkedIn](https://www.linkedin.com/in/demetriosalvess)
