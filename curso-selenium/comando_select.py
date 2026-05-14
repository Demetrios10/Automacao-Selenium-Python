import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://webflow.com/made-in-webflow/animation")
time.sleep(10)

dropdow_marketplace = browser.find_element(By.XPATH,"wf-1rzwxxs --styled-kANgyy wf-xflg4e")
dropdow_marketplace.click()
dropdow_marketplace.select_by_visible_text("Overview")


