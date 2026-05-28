from selenium.webdriver.common.by import By
import pytest
import conftest


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestCT01:
    def test_ct01_adicionar_produtos_carrinho(self):
     driver = conftest.driver
     driver.find_element(By.ID, "user-name").send_keys("standard_user")
     driver.find_element(By.ID, "password").send_keys("secret_sauce")
     driver.find_element(By.ID, "login-button").click()

     driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div").click()

     driver.find_element(By.XPATH, "//button[@id='add-to-cart']").click()

     # clicando no carrinho para verificar se o produto esta selecionado
     driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()

     # acionando botão para voltar para tela de produtos
     driver.find_element(By.ID, "continue-shopping").click()

     # adicionando mais um produto ao carrinho
     driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
     driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()


     assert driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']").is_displayed()
     assert driver.find_element(By.XPATH, "//div[text()='Sauce Labs Bike Light']").is_displayed()







