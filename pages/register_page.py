"""Page Object do formulário Automation Demo Site."""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class RegisterPage:
    URL = "https://demo.automationtesting.in/Register.html"
    CAMPOS = {
        "nome": (By.CSS_SELECTOR, "input[placeholder='First Name']"),
        "sobrenome": (By.CSS_SELECTOR, "input[placeholder='Last Name']"),
        "endereco": (By.CSS_SELECTOR, "textarea"),
        "email": (By.CSS_SELECTOR, "input[type='email']"),
        "telefone": (By.CSS_SELECTOR, "input[type='tel']"),
        "senha": (By.ID, "firstpassword"),
        "confirmacao": (By.ID, "secondpassword"),
    }
    GENEROS = {"masculino": "Male", "feminino": "FeMale"}
    HOBBIES = {"cricket": "checkbox1", "filmes": "checkbox2", "hockey": "checkbox3"}

    def __init__(self, browser, timeout=20):
        self.browser = browser
        self.wait = WebDriverWait(browser, timeout)

    def abrir(self):
        self.browser.get(self.URL)
        self.wait.until(EC.visibility_of_element_located(self.CAMPOS["nome"]))
        return self

    def campo(self, nome):
        if nome not in self.CAMPOS:
            raise ValueError(f"Campo desconhecido: {nome}")
        return self.wait.until(EC.visibility_of_element_located(self.CAMPOS[nome]))

    def preencher(self, **dados):
        desconhecidos = set(dados) - self.CAMPOS.keys()
        if desconhecidos:
            raise ValueError(f"Campos desconhecidos: {sorted(desconhecidos)}")
        for nome, valor in dados.items():
            campo = self.campo(nome)
            campo.clear()
            campo.send_keys(valor)
            campo.send_keys(Keys.TAB)
        return self

    def valor(self, nome):
        return self.campo(nome).get_property("value")

    def validade(self, nome):
        return self.campo(nome).get_property("validity")

    def genero(self, nome):
        if nome not in self.GENEROS:
            raise ValueError("Gênero desconhecido.")
        return self.browser.find_element(
            By.CSS_SELECTOR, f"input[name='radiooptions'][value='{self.GENEROS[nome]}']")

    def selecionar_genero(self, nome):
        self.genero(nome).click()
        return self

    def hobby(self, nome):
        if nome not in self.HOBBIES:
            raise ValueError("Hobby desconhecido.")
        return self.browser.find_element(By.ID, self.HOBBIES[nome])

    def definir_hobby(self, nome, marcado=True):
        campo = self.hobby(nome)
        if campo.is_selected() != marcado:
            campo.click()
        return self

    def atualizar(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "Button1"))).click()
        self.wait.until(lambda _: self.valor("nome") == "")
        return self
