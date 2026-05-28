import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.implicitly_wait(12)  # espera até 12 segundos para encontrar o elemento

browser.maximize_window()
browser.get("https://www.chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

clica_botao = browser.find_element(By.ID,"display-other-button")
clica_botao.click()
time.sleep(12)

botao_aparente = browser.find_element(By.ID,"display-other-button")
botao_aparente.click()
assert botao_aparente.is_displayed()
print("Botão aparente em tela")


