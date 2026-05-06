import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# get() é o comando para acessar um site 
browser = webdriver.Chrome()
browser.get("https://www.saucedemo.com/")
browser.maximize_window()
time.sleep(5)

# send_keys() é o comando para enviar texto para um elemento
campo_usuario = browser.find_element(By.ID, "user-name")
campo_password = browser.find_element(By.ID, "password")

campo_usuario.send_keys("standard_user")
campo_password.send_keys("secret_sauce")


botao_login = browser.find_element(By.ID, "login-button")
botao_login.click() # click() é o comando para clicar em um elemento
time.sleep(5)

# text() é o comando para obter o texto de um elemento
titulo_pagina = browser.find_element(By.CLASS_NAME, "title")
print(titulo_pagina.text)
assert titulo_pagina.text == "Products", "O título da página não é 'Produtos'"

# get_attribute() é o comando para obter o valor de um atributo de um elemento
img = browser.find_element(By.CLASS_NAME, "inventory_item_img")
print(img.get_attribute("class"))
assert img.get_attribute("class") == "inventory_item_img"
