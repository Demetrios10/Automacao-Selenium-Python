import time
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()

browser.get('https://www.youtube.com')
browser.maximize_window()

insere_texto = browser.find_element('xpath', '//*[@id="center"]/yt-searchbox/div[1]/div/div/form/input')
insere_texto.send_keys('barcelona')
time.sleep(3)

clica_lupa = browser.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/div/button/span/span/div')
clica_lupa.click()
time.sleep(5)


browser.quit()