# Relatório — Cadastro com POM

Data: 07/11/2026.

## Execução padrão

`python -m unittest discover -s tests -v`

19 testes descobertos: 8 unitários aprovados e 11 E2E ignorados por exigirem RUN_E2E=1. Duração: 0,007 s. Os unitários usam simulação e não comprovam o funcionamento do formulário no navegador.

## Tentativa real

Executado `test_nome_e_sobrenome` com RUN_E2E=1 e Chrome visível. Resultado: erro na criação da sessão Chrome (`SessionNotCreatedException`, `DevToolsActivePort file doesn't exist`). O site não chegou a ser aberto. Os outros dez cenários reais não foram executados após esse bloqueio.

## Base dos cenários

HTML consultado diretamente em https://demo.automationtesting.in/Register.html. Seletores confirmados no HTML: placeholders de nome/sobrenome, input de e-mail e telefone, IDs firstpassword/secondpassword/checkbox1–3/Button1 e radiooptions. Telefone exige dez dígitos; confirmação de senha usa validação customizada no evento blur.

## Limites

Não foi validado cadastro no servidor, nem afirmado sucesso dos cenários E2E. País, idiomas, habilidades, data de nascimento e upload ainda não fazem parte dos cenários automatizados.
