import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# get() é o comando para acessar um site 
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demo.applitools.com/")
time.sleep(5)

username = browser.find_element(By.ID, "username")
checkbox = browser.find_element(By.XPATH, "//input[@type='checkbox' and @class='form-check-input']")

# is_displayed() é o comando para verificar se um elemento está visível na tela
if username.is_displayed():
    print("O campo de username está visível na tela.")

# is_enabled() é o comando para verificar se um elemento está habilitado para interação
if checkbox.is_enabled():
    print("O checkbox está habilitado para interação.")

# is_selected() é o comando para verificar se um elemento do tipo checkbox ou radio button está selecionado
if checkbox.is_selected():
    print("O checkbox está selecionado.")
else:
    print("O checkbox não está selecionado.")
    
# click() é o comando para clicar em um elemento
time.sleep(2)
checkbox.click()
if checkbox.is_selected():
 print("O checkbox está selecionado.")