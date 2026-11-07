# Relatório de testes

Execução em 07/11/2026.

## Resultado

- Comando: `python -m unittest discover -s tests -v`
- Total: 18 testes (14 novos e 4 existentes).
- Resultado: 18 aprovados, 0 falhas, 0 erros.
- Duração reportada pelo unittest: 0,204 s.
- Ambiente: Windows, Python 3.14 e Selenium 4.43.0.

## Cobertura dos novos cenários

- Pesquisa com envio por Enter e limpeza do campo.
- Remoção de espaços nas extremidades do termo.
- Termos com acentos, espaços e símbolos na URL.
- Termo vazio ou contendo apenas espaços.
- Tempo limite zero ou negativo.
- URL com termo diferente e página que não é de resultados.
- Campo de pesquisa desabilitado.
- Nenhum vídeo disponível.
- Exclusão de títulos vazios e vídeos ocultos.
- Resultados carregados após tentativas iniciais vazias.
- Falha de navegação.
- Modo sem janela e tempo limite personalizados.
- Modo padrão com janela.

## Limites

Os 18 testes usam navegador/DOM simulados. As condições e esperas da busca são executadas com WebDriverWait real em tempo reduzido. Não foi comprovada a integração com YouTube.

A tentativa de execução com Chrome encontrou falha de acesso ao cache/obtenção do driver e não concluiu a inicialização dentro do limite externo de 25 segundos. Isso é um bloqueio do ambiente, não um teste E2E aprovado.
