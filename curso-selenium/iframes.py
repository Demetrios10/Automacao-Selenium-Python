import time
from selenium import webdriver
from selenium.webdriver.common.by import By



browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.gov.br/ds/home")
time.sleep(10)