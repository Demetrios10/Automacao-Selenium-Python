# language: pt
Funcionalidade: Login
  Como um usuário
  Quero fazer login no sistema
  Para acessar minha conta

  Cenário: Login válido
    Dado que estou na página de login
    Quando preencho o email com "usuario@teste.com"
    E preencho a senha com "senha123"
    E clico no botão de login
    Então devo ser redirecionado para a página inicial

  Cenário: Login com credenciais inválidas
    Dado que estou na página de login
    Quando preencho o email com "usuario@teste.com"
    E preencho a senha com "senhaerrada"
    E clico no botão de login
    Então devo ver a mensagem de erro "Credenciais inválidas"
