from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(5)

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div").click()

driver.find_element(By.XPATH,"//button[@id='add-to-cart']").click()

# cicando no carrinho para verificar se o produto esta selecionado
driver.find_element(By.XPATH,"//*[@class='shopping_cart_link']").click()
time.sleep(10)

# clicando no botão para finalizar a compra
driver.find_element(By.ID,"checkout").click()
time.sleep(5)

# preenchendo os campos para finalizar a compra
driver.find_element(By.ID,"first-name").send_keys("Demetrios")
driver.find_element(By.ID,"last-name").send_keys("Alves da Silva")
driver.find_element(By.ID,"postal-code").send_keys("04653130")
time.sleep(5)

# clicando no botão Continue
driver.find_element(By.ID,"continue").click()

# clicando no botão Finish
driver.find_element(By.ID,"finish").click()
time.sleep(5)

# verificando se o texto esta na tela
assert driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/span").is_displayed()

# salva a evidência
driver.save_screenshot("evidencias/compra_de_1_produto.png")

driver.quit()
