# Primeiro importe o webdriver que é o módulo que provê implementações para diferentes browsers.
from selenium import webdriver

# Crie uma instância do navegador que vamos utiliza, passando o caminho do webdriver baixado.
chrome = webdriver.Chrome('chromedriver_win32/chromedriver.exe')

# Com a instância do webdriver podemos utilizar o método 'get' para abrir a página especificada.
chrome.get('https://www.python.org/')