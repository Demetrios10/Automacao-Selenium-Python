# O Comando assert é utilizado para validar se um elemento ou uma ação ocorreu como esperado.
# Ele é muito útil para garantir que o teste esteja funcionando corretamente e para identificar
# falhas no código.

# assert numbers
numero1 = 1
numero2 = 20
assert numero1 < numero2, f"O {numero1} deve ser menor que o {numero2}"
print("O assert de números passou com sucesso!")
if numero1 > numero2:
    raise AssertionError(f"O {numero1} deve ser menor que o {numero2}")


# assert text
texto_esperado = 'Olá, mundo!'
texto_obtido = 'Olá, mundo!'
assert texto_obtido == texto_esperado, f"O texto obtido '{texto_obtido}' é diferente do texto esperado '{texto_esperado}'"
print("O assert de texto passou com sucesso!")


# assert text in string
frase = "O céu é azul"
assert "azul" in frase, f"A palavra 'azul' não está presente na frase '{frase}'"
print("O assert de texto em string passou com sucesso!")



