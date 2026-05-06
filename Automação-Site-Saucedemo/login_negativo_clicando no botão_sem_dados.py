# login no site saucedemo

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Inicializa o driver (ex: Chrome)
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(3)

# clicando no botão login
botao_login = driver.find_element(By.XPATH,"//input[@type='submit' and @data-test='login-button']")
botao_login.click()
time.sleep(5)





