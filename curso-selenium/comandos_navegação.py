import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# get() é o comando para acessar um site 
browser = webdriver.Chrome()
browser.get("https://google.com")

# maximize_window() maximiza a tela do navegador para facilitar a visualização
browser.maximize_window()

# minimiza a janela do navegador para mostrar que o comando funciona, mas não é recomendado usar em testes automatizados, pois pode interferir na execução dos testes
browser.minimize_window()
time.sleep(5)

# refresh() atualiza a pagina atual
browser.refresh()
time.sleep(3)

# get() é o comando para acessar um site 
browser.get("https://nike.com.br")

# back() navega para a página anterior
browser.back()
time.sleep(5)

# forward() navega para a próxima página, caso tenha voltado para a página anterior usando back()
browser.forward()
time.sleep(5)

# switch_to.new_window() abre uma nova aba ou janela do navegador, dependendo do argumento passado ('tab' para nova aba e 'window' para nova janela)
# browser.switch_to.new_window('tab')
# browser.get("https://youtube.com")

# close() fecha a aba atual do navegador
# browser.close()

# quit() fecha todas as abas e janelas do navegador, encerrando a sessão do WebDriver
browser.switch_to.new_window('tab')
browser.switch_to.new_window('tab')
time.sleep(10)
browser.quit()
