# Evidências de execução

- `unitarios.txt`: saída real dos oito testes unitários desta entrega.
- `tentativa-navegador.txt`: registro da tentativa real de abrir o Chrome nesta entrega.
- `execucoes/`: gerada automaticamente pelos testes E2E, com uma pasta UTC por cenário.

Quando o Chrome abre, são salvos `tela-final.png` e `pagina.txt`. Se a inicialização falha, é salvo `erro.txt`; não há captura de um navegador que não abriu.

A captura mostra o estado final e não comprova aprovação por si só. O resultado vem do relatório do executor. Não há gravação de vídeo ou captura de cada ação intermediária.

As execuções locais geradas em `execucoes/` são ignoradas pelo Git. Os registros desta entrega estão versionados aqui. Não existem evidências recuperáveis das execuções antigas além dos relatórios já documentados.

## Resultado por cenário

A classe EvidenceTestCase registra resultado.json para todos os cenários unittest, incluindo testes unitários e testes reais ignorados. O E2E também captura o estado final quando o navegador abre.

## Revisão em 12/11/2026

A pasta [revisao-2026-11-12](revisao-2026-11-12) contém uma evidência por cenário da rodada de verificação desta revisão. Resultados aprovados, ignorados e falhas são distintos. Somente cenários com navegador disponível têm captura. As próximas execuções continuam em execucoes/.
