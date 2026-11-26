"""Page Object do formulário Automation Demo Site."""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

ROLAR_ATE_O_TOPO = "arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});"


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
    BOTAO_ATUALIZAR = (By.ID, "Button1")

    def __init__(self, browser, timeout: float = 20) -> None:
        self.browser = browser
        self.wait = WebDriverWait(browser, timeout)

    def abrir(self) -> "RegisterPage":
        self.browser.get(self.URL)
        self.wait.until(ec.visibility_of_element_located(self.CAMPOS["nome"]))
        return self

    def campo(self, nome: str):
        _exigir_opcao(self.CAMPOS, nome, f"Campo desconhecido: {nome}")
        return self.wait.until(ec.visibility_of_element_located(self.CAMPOS[nome]))

    def preencher(self, **dados: str) -> "RegisterPage":
        # Valida todo o payload antes de modificar o formulário.
        self._validar_dados(dados)
        for nome, valor in dados.items():
            self._digitar(self.campo(nome), valor)
        return self

    def valor(self, nome: str) -> str:
        return self.campo(nome).get_property("value")

    def validade(self, nome: str) -> dict:
        return self.campo(nome).get_property("validity")

    def genero(self, nome: str):
        _exigir_opcao(self.GENEROS, nome, "Gênero desconhecido.")
        seletor = f"input[name='radiooptions'][value='{self.GENEROS[nome]}']"
        return self.browser.find_element(By.CSS_SELECTOR, seletor)

    def selecionar_genero(self, nome: str) -> "RegisterPage":
        self.genero(nome).click()
        return self

    def hobby(self, nome: str):
        _exigir_opcao(self.HOBBIES, nome, "Hobby desconhecido.")
        return self.browser.find_element(By.ID, self.HOBBIES[nome])

    def definir_hobby(self, nome: str, marcado: bool = True) -> "RegisterPage":
        campo = self.hobby(nome)
        if campo.is_selected() != marcado:
            # Posiciona o controle fora de sobreposições flutuantes quando possível.
            self.browser.execute_script(ROLAR_ATE_O_TOPO, campo)
            campo.click()
        return self

    def atualizar(self) -> "RegisterPage":
        self.wait.until(ec.element_to_be_clickable(self.BOTAO_ATUALIZAR)).click()
        self.wait.until(lambda _: self.valor("nome") == "")
        return self

    def _validar_dados(self, dados: dict) -> None:
        desconhecidos = set(dados) - self.CAMPOS.keys()
        if desconhecidos:
            raise ValueError(f"Campos desconhecidos: {sorted(desconhecidos)}")
        sem_valor = sorted(nome for nome, valor in dados.items() if valor is None)
        if sem_valor:
            raise ValueError(f"Campos com valor None: {sem_valor}")

    @staticmethod
    def _digitar(campo, valor: str) -> None:
        campo.clear()
        campo.send_keys(valor)
        campo.send_keys(Keys.TAB)


def _exigir_opcao(opcoes: dict, nome: str, mensagem: str) -> None:
    if nome not in opcoes:
        raise ValueError(mensagem)
