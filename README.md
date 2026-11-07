# Automação web com Selenium e Python

Exemplo de estudo que abre o YouTube no Chrome, pesquisa por `barcelona` e encerra o navegador.

## Estrutura

```text
scripts/
└── pesquisa_youtube.py
requirements.txt
README.md
```

## Preparação

Tenha Python 3, Google Chrome e conexão com a internet disponíveis.

```bash
git clone https://github.com/Demetrios10/Automacao-Selenium-Python.git
cd Automacao-Selenium-Python
python -m venv .venv
```

Ative o ambiente no Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

Instale a dependência e execute:

```bash
python -m pip install -r requirements.txt
python scripts/pesquisa_youtube.py
```

O Selenium pode precisar baixar o driver compatível com o Chrome na primeira execução.

## Funcionamento e limites

O script original foi preservado e movido para `scripts/pesquisa_youtube.py` (antes `test_pesquisa_youtube.py`). É um script demonstrativo, sem asserções automatizadas. Ele utiliza seletores XPath e pausas fixas; mudanças no YouTube ou telas de consentimento podem impedir a execução.

## Próximas melhorias

- Usar esperas explícitas
- Adicionar validação dos resultados
- Garantir o encerramento do navegador em caso de erro
- Evoluir para testes com pytest

## Autor

[Demétrios Alves Da Silva](https://github.com/Demetrios10)
