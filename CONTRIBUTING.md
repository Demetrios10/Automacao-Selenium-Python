# Desenvolvimento e contribuição

## Organização

Mantenha seletores, ações e leitura de estado em `pages/`; gerenciamento de sessão em `core/`; fluxos demonstrativos em `scripts/`; asserções em `tests/`. Use dados fictícios e preserve o escopo sem envio de cadastro ao servidor.

## Validar mudanças

Execute a suíte padrão com `python -m unittest discover -s tests -v`. Para alterações de comportamento da página, habilite `RUN_E2E=1` e execute os cenários reais quando houver Chrome funcional. Registre a distinção entre unitário com mock, E2E ignorado, falha de ambiente e comportamento efetivamente verificado.

Prefira esperas explícitas baseadas no estado da página. Preserve isolamento por sessão e encerramento do navegador. Não remova uma falha real das evidências para apresentar uma simulação como sucesso.

## Documentar uma execução

Informe data, versões de Python/Chrome/Selenium, sistema, comando, modo headless e resultado. Remova dados pessoais e credenciais de logs e imagens. Não reescreva relatórios históricos como se fossem uma nova execução.

Antes de propor um cenário, confira a regra no formulário e defina uma asserção observável. Testes de criação de conta ou envio externo exigem revisão explícita do escopo.
