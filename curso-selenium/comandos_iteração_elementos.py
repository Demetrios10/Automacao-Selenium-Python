import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# get() é o comando para acessar um site 
browser = webdriver.Chrome()
browser.get("https://www.saucedemo.com/")
browser.maximize_window()
time.sleep(5)