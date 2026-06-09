import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains , Keys


class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)

    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)

    def escrever(self, locator, text):
        self.encontrar_elemento(locator).send_keys(text)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()

    def verificar_se_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator).is_displayed()

    def pegar_texto_elemento(self, locator):
        self.esperar_elemento_visivel(locator)
        return self.encontrar_elemento(locator).text

    def esperar_elemento_visivel(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(*locator))

    # verificar se um elemento existe na página
    def verificar_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator), f"Elemento não encontrado: {locator} não existe mais é esperado que existe."

    # verificar se um elemento não existe na página
    def verificar_elemento_nao_existe(self, locator):
        assert len(self.encontrar_elementos(locator)) == 0, f"Elemento encontrado: {locator} existe mais é esperado que não existe."

    # clicar duas vezes em um elemento
    def clicar_duas_vezes(self, locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).double_click(element).perform()

    # clicar com o botão direito em um elemento
    def clique_botao_direito(self, locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).context_click(element).perform()

    def precionar_tecla(self, locator, key):
        element = self.encontrar_elemento(locator)
        if key.lower() == "enter":
            element.send_keys(Keys.ENTER)
        elif key.lower() == "tab":
            element.send_keys(Keys.TAB)
        elif key.lower() == "esc":
            element.send_keys(Keys.ESCAPE)
        else:
            raise ValueError(f"Tecla não suportada: {key}")
        return self.encontrar_elemento(locator).text
