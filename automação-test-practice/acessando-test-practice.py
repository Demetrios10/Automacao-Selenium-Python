# Acessando Site test pratctice

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o driver (ex: Chrome)
driver = webdriver.Chrome()
driver.get("https://leogcarvalho.github.io/test-automation-practice/")
time.sleep(3)

# clicando botão conecte-se sem preencher com os dados 
botao_conecte_se = driver.find_element(By.ID,"login-button")
botao_conecte_se.click()
time.sleep(3)
