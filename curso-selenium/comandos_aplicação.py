import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# get() é o comando para acessar um site 
browser = webdriver.Chrome()
browser.get("https://www.saucedemo.com/")
time.sleep(5)

# Imprime o título da página
print("Esse é o titulo da pagina:",browser.title) 

# current_url é o comando para imprimir a url atual
print("Essa é a url atual:","https://www.saucedemo.com/" )

# page_source é o comando para imprimir o código fonte da página
print("Esse é o código fonte da página:", browser.page_source)

