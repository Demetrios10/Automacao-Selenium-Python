# Estudo de caso · Automação com Selenium

[README e execução](../README.md) · [Portfólio do autor](https://github.com/Demetrios10/Demetrios10/blob/main/PORTFOLIO.md)

## Problema e objetivo

Validar campos e estados de um formulário web com cenários legíveis, evitando concentrar seletores, infraestrutura e asserções no mesmo script. O exercício usa dados fictícios e não envia o cadastro ao servidor.

## Solução e decisões

O Page Object encapsula seletores, ações e leitura de estado. O gerenciador do Chrome cuida do ciclo da sessão. A demonstração apresenta o fluxo, enquanto as regras verificadas ficam nos testes.

As esperas são explícitas. Cada cenário E2E usa uma sessão própria; o encerramento e a captura de evidências ficam registrados como limpeza da execução. Os unitários usam mocks para verificar o contrato do Page Object sem depender do site externo.

## O que revisar no código

| Arquivo | O que demonstra |
|---|---|
| [Page Object](../pages/register_page.py) | Ações, seletores e leitura da validade dos campos |
| [Sessão do navegador](../core/browser.py) | Inicialização e encerramento do Chrome |
| [Evidências](../core/evidencias.py) | Organização de erros e capturas |
| [Unitários](../tests/test_register_page.py) | Validações e comportamento com mocks |
| [Cenários E2E](../tests/test_register_e2e.py) | Asserções no formulário e isolamento das sessões |

## Evidência e limites

O [relatório de 07/11/2026](RELATORIO-TESTES.md) registra oito unitários aprovados. Onze cenários E2E estão definidos: nomes, e-mail, telefone, gênero, hobbies, senhas e limpeza do formulário.

A tentativa real registrada falhou ao inicializar o Chrome; os cenários E2E permanecem sem validação bem-sucedida. A execução padrão ignora esses casos até habilitar `RUN_E2E=1`. Aprovação dos unitários com mocks não comprova funcionamento no navegador.

O site externo contém recursos HTTP em uma página HTTPS e pode sofrer bloqueios ou indisponibilidade. O fluxo não comprova persistência de cadastro no backend. Nesta revisão do portfólio, os testes foram consultados e a documentação ajustada; não houve nova execução.

## Próxima evolução

Executar os 11 casos com Chrome funcional, registrar ambiente e resultados e investigar os recursos externos antes de preparar uma execução contínua.

Revisão: 09/11/2026.
