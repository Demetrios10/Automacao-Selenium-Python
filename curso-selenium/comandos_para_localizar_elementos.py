import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# get() é o comando para acessar um site 
browser = webdriver.Chrome()
browser.get("https://saucedemo.com/")
browser.maximize_window()
time.sleep(5)

# find_element() é o comando para localizar um elemento na página, ele tem dois parâmetros: o primeiro é o tipo de localização (By.ID, By.NAME, By.XPATH, etc) e o segundo é o valor da localização (o id, nome, xpath, etc do elemento)
usuario = browser.find_element(By.ID, "user-name")
senha = browser.find_element(By.ID, "password")

# send_keys() é o comando para enviar texto para um elemento, ele tem um parâmetro que é o texto a ser enviado
# usuario.send_keys("standard_user")
# senha.send_keys("secret_sauce")
# time.sleep(5)
# browser.quit()

# find_elements() é o comando para localizar vários elementos na página, ele tem os mesmos parâmetros do find_element() e retorna uma lista de elementos encontrados
autenticacao_varios_elementos = browser.find_elements(By.XPATH, "//input[contains(@class,'form_input') and @name='user-name']")
print(autenticacao_varios_elementos)
print(len(autenticacao_varios_elementos))
assert len(autenticacao_varios_elementos) == 2, "O número de elementos encontrados é diferente de 2"