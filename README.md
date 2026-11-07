# Automação web com Selenium e Python

**Python · Selenium WebDriver · QA**

Fluxo de pesquisa no YouTube com validação da URL e de vídeos visíveis, esperas explícitas e encerramento do navegador mesmo em caso de falha.

## Preparação

Requisitos: Python 3, Google Chrome e internet. O Selenium pode baixar o driver na primeira execução.

```bash
git clone https://github.com/Demetrios10/Automacao-Selenium-Python.git
cd Automacao-Selenium-Python
python -m venv .venv
```

Ative o ambiente no PowerShell: `.\.venv\Scripts\Activate.ps1`. No Linux/macOS: `source .venv/bin/activate`.

```bash
python -m pip install -r requirements.txt
python scripts/pesquisa_youtube.py
python scripts/pesquisa_youtube.py --termo "testes de software" --headless --timeout 30
```

## O que é validado

1. O campo de pesquisa está disponível para interação.
2. A URL de resultados contém exatamente o termo enviado.
3. Pelo menos um título de vídeo está visível.

A execução imprime até cinco títulos. Se a validação expirar, o processo termina com erro e encerra o navegador. Não é verificada a relevância semântica dos vídeos.

## Testes locais sem navegador

```bash
python -m unittest discover -s tests -v
```

A suíte contém 18 testes: fechamento do navegador, termos com espaços e acentos, entradas inválidas, URL incorreta, campo desabilitado, ausência de vídeos, títulos vazios/ocultos, carregamento tardio e configuração headless. Usa DOM simulado e esperas do Selenium; não comprova o funcionamento do YouTube real. Consulte o [relatório de execução](docs/RELATORIO-TESTES.md).

## Estrutura

- `scripts/pesquisa_youtube.py`: fluxo, validações e interface de linha de comando.
- `tests/test_execucao.py`: verificações do ciclo de vida do navegador.
- `tests/test_pesquisa.py`: cenários de busca, espera e configuração.
- `requirements.txt`: dependências.

## Limitações e próximos passos

YouTube é um serviço externo: seletores, consentimento de cookies, bloqueios e disponibilidade podem afetar a execução. O script não contorna consentimento ou CAPTCHA. A execução real precisa ser validada no ambiente de destino.

Próximos passos: cenários com pytest, evidências de falha e integração contínua com um site de teste controlado.

## Contexto profissional

Projeto de estudo de Demétrios Alves da Silva, QA Analyst com experiência em pagamentos, serviços financeiros e seguros.

[Perfil no GitHub](https://github.com/Demetrios10) · [LinkedIn](https://www.linkedin.com/in/demetriosalvess)
