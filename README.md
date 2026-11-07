# Automação de cadastro — Selenium + POM

Projeto de estudos em QA para https://demo.automationtesting.in/Register.html.

## Instalação

Requer Python 3, Chrome e acesso à internet.

```bash
python -m venv .venv
python -m pip install -r requirements.txt
```

Ative o ambiente antes de instalar: no PowerShell, `.\.venv\Scripts\Activate.ps1`; em Linux/macOS, `source .venv/bin/activate`.

## Executar demonstração com navegador

```bash
python -m scripts.cadastro
```

Preenche dados fictícios e valida a leitura dos campos, sem enviar cadastro. Use `--headless` para ocultar a janela.

## Testes

Suíte padrão (testes unitários; E2E aparecem como ignorados):

```bash
python -m unittest discover -s tests -v
```

Testes reais no PowerShell:

```powershell
$env:RUN_E2E = "1"
python -m unittest discover -s tests -p test_register_e2e.py -v
Remove-Item Env:RUN_E2E
```

Opcional: `$env:HEADLESS = "1"`. Cada cenário abre sua própria sessão Chrome.

## Estrutura POM

- `pages/register_page.py`: seletores, ações e estado do formulário.
- `core/browser.py`: criação e encerramento do navegador.
- `scripts/cadastro.py`: demonstração do fluxo.
- `tests/test_register_page.py`: 8 testes unitários.
- `tests/test_register_e2e.py`: 11 cenários reais do formulário.
- `docs/RELATORIO-TESTES.md`: resultados e limitações.

As asserções ficam nos testes. A página encapsula ações e leitura de estado.

## Cenários reais

Nome e sobrenome; nome obrigatório; e-mail válido/inválido; telefone de 9/10 dígitos; exclusividade de gênero; múltiplos hobbies; senhas iguais/diferentes; limpeza pelo botão Refresh.

As regras verificadas vêm do HTML e do JavaScript do formulário, incluindo telefone com exatamente dez dígitos. Não há teste de cadastro bem-sucedido nem envio de dados ao servidor.

## Limitações

O site usa dependências HTTP em uma página HTTPS, que podem ser bloqueadas pelo navegador. Recursos dinâmicos, lista de países e backend podem falhar. Os cenários reais devem registrar essas falhas; não são substituídos por simulações aprovadas.

O fluxo anterior de YouTube foi substituído no código ativo. Seu histórico permanece nos commits do GitHub.

## Autor

[Demétrios Alves da Silva](https://github.com/Demetrios10) · [LinkedIn](https://www.linkedin.com/in/demetriosalvess)
