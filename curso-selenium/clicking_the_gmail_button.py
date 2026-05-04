import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://google.com")
time.sleep(5)

# clicando botão gmail
gmail = browser.find_element(By.XPATH,"//a[normalize-space()='Gmail']")
gmail.click()
time.sleep(5)