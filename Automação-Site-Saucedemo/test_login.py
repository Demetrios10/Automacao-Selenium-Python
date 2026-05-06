import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from login_page import LoginPage

# ===== CONFIG =====
URL = "https://www.saucedemo.com/"
EVIDENCE_DIR = "evidencias"

# cria pasta se não existir
os.makedirs(EVIDENCE_DIR, exist_ok=True)

def take_screenshot(driver, step_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{EVIDENCE_DIR}/{timestamp}_{step_name}.png"
    driver.save_screenshot(file_name)

# ===== TEST =====
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # acesso ao site
    driver.get(URL)
    take_screenshot(driver, "01_home")

    # login
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    take_screenshot(driver, "02_login_realizado")

    # validação
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
    take_screenshot(driver, "03_pos_login")

    assert "Products" in driver.page_source

    # ação extra (ex: filtro)
    filtro = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='product-sort-container']"))
    )
    filtro.click()
    take_screenshot(driver, "04_filtro_clicado")

except Exception as e:
    # screenshot em caso de erro
    take_screenshot(driver, "ERRO")
    print(f"Erro durante execução: {e}")
    raise

finally:
    driver.quit()






