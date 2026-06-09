"""
Factory para criar instâncias do WebDriver
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os


class DriverFactory:
    """Factory para gerenciar WebDriver"""
    
    @staticmethod
    def criar_driver_chrome():
        """Cria uma instância do Chrome WebDriver"""
        opcoes = Options()
        
        # Configurações opcionais
        # opcoes.add_argument('--headless')  # Descomentar para modo headless
        opcoes.add_argument('--start-maximized')
        opcoes.add_argument('--disable-notifications')
        opcoes.add_argument('--disable-popup-blocking')
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=opcoes)
        
        return driver
    
    @staticmethod
    def sair_driver(driver):
        """Fecha o driver"""
        if driver:
            driver.quit()


class ScreenshotUtils:
    """Utilidades para captura de telas"""
    
    @staticmethod
    def tirar_screenshot(driver, nome_arquivo):
        """Tira um screenshot e salva em screenshots/"""
        screenshots_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'screenshots')
        
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        
        caminho_arquivo = os.path.join(screenshots_dir, f"{nome_arquivo}.png")
        driver.save_screenshot(caminho_arquivo)
        
        return caminho_arquivo
