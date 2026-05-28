import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
wait = WebDriverWait(browser, 30)

# alert is present
# browser.find_element(By.ID,"alert").click()
# wait.until(EC.alert_is_present())
# time.sleep(15)

# text to be present in element
# browser.find_element(By.ID,"populate-text").click()
# wait.until(EC.text_to_be_present_in_element((By.XPATH,"//*[text()='Selenium WebDriver']") ,"Selenium Webdriver"))
# target_text = browser.find_element(By.XPATH,"//*[text()='Selenium Webdriver']").text
#assert target_text == "Selenium Webdriver"
# time.sleep(5)

# element to be clickable
browser.find_element(By.ID,"enable-button").click()
wait.until(EC.element_to_be_clickable((By.ID,"disable")))
time.sleep(5)
assert browser.find_element(By.ID,"disable").is_enabled() == True
print("Button is enabled")


# element to be selected
browser.find_element(By.ID,"checkbox").click()
time.sleep(5)
wait.until(EC.element_to_be_selected((browser.find_element(By.ID,"ch"))))
time.sleep(5)
assert browser.find_element(By.ID,"ch").is_selected() == True
print("Checkbox is selected")

