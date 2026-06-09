# Configurações e Fixtures do Pytest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os
import sys
from datetime import datetime

# Adicionar utils ao path
sys.path.insert(0, os.path.dirname(__file__))

from utils.driver_factory import DriverFactory, ScreenshotUtils


@pytest.fixture(scope="function")
def driver():
    """Fixture que fornece instância do Chrome WebDriver"""
    driver_instance = DriverFactory.criar_driver_chrome()
    driver_instance.implicitly_wait(10)
    
    yield driver_instance
    
    # Teardown
    DriverFactory.sair_driver(driver_instance)


@pytest.fixture(scope="function")
def driver_com_screenshot(driver, request):
    """Fixture que captura screenshot em caso de falha"""
    yield driver
    
    # Captura screenshot se o teste falhou
    if request.node.rep_call.failed:
        nome_screenshot = f"falha_{request.node.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        ScreenshotUtils.tirar_screenshot(driver, nome_screenshot)


@pytest.fixture(scope="function")
def setup_teardown():
    """Fixture compatível com testes legados"""
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    yield

    driver.quit()


# Hook para capturar resultado do teste
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook para rastrear resultado dos testes"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
    
