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
time.sleep(5)

driver.find_element(By.XPATH, "//button[contains(@class,'btn_inventory') and @data-test='add-to-cart-sauce-labs-backpack']").click()
time.sleep(5)
