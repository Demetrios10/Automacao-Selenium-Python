# Padrões de automação e evidências

Revisão em 12/11/2026.

## Interface e POM

As páginas encapsulam seletores e operações de interface. Os testes mantêm os cenários e as asserções. A sessão do navegador e o registro de evidências ficam separados.

## Evidências

Cada cenário tem uma pasta em evidencias/execucoes, com um resultado.json. Cenários ignorados são identificados como ignorados, nunca como aprovados. Capturas só existem se houver uma sessão de navegador disponível; testes de API usam o registro estruturado.

As execuções geradas permanecem locais e são ignoradas pelo Git. Os relatórios de revisão descrevem o que foi realmente executado.
