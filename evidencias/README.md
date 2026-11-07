# Evidências de execução

- `unitarios.txt`: saída real dos oito testes unitários desta entrega.
- `tentativa-navegador.txt`: registro da tentativa real de abrir o Chrome nesta entrega.
- `execucoes/`: gerada automaticamente pelos testes E2E, com uma pasta UTC por cenário.

Quando o Chrome abre, são salvos `tela-final.png` e `pagina.txt`. Se a inicialização falha, é salvo `erro.txt`; não há captura de um navegador que não abriu.

A captura mostra o estado final e não comprova aprovação por si só. O resultado vem do relatório do executor. Não há gravação de vídeo ou captura de cada ação intermediária.

As execuções locais geradas em `execucoes/` são ignoradas pelo Git. Os registros desta entrega estão versionados aqui. Não existem evidências recuperáveis das execuções antigas além dos relatórios já documentados.
