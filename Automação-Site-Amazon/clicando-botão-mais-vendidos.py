# Acessando Site Amazon

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o driver (ex: Chrome)
driver = webdriver.Chrome()
driver.get("https://www.amazon.com.br")
time.sleep(5)

# clicando no botão todos
botao_todos = driver.find_element(By.ID,"nav-hamburger-menu")
botao_todos.click()
time.sleep(5)

# clicando no botão mais vendidos
botao_mais_vendidos = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div[1]/section[1]/ul/li[1]/a")
botao_mais_vendidos.click()
time.sleep(3)


