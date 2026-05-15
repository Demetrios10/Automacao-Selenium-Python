import time
from selenium import webdriver
from selenium.webdriver.common.by import By



browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demo.automationtesting.in/Frames.html")
time.sleep(10)

browser.find_element(By.XPATH, '//a[@href="#Multiple"]').click()
time.sleep(10)


Iframe1 = browser.find_element(By.XPATH,"container iframes-page-container")
browser.switch_to(Iframe1)
browser = browser.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("Iframe1")




