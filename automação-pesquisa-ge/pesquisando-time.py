import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://ge.globo.com/")
driver.maximize_window()

busca = driver.find_element(By.ID, "busca-campo")
busca.send_keys("São Paulo")
time.sleep(10)

lupa = driver.find_element(By.XPATH, "//div[@class='featured-content__title']")
lupa.click()
time.sleep(10)



