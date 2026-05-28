import time
from selenium import webdriver
from selenium.webdriver.common.by import By



browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.gov.br/ds/home")
time.sleep(10)

browser = browser.find_element(By.XPATH,"/html/body/br-root/main/div/div/br-menu/div/div/div/div/nav/div[1]/a").click()
time.sleep(5)






