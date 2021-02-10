# importando as bibliotecas
import requests
from bs4 import BeautifulSoup

# Realiza uma requisição do tipo get na url indicada
req_get = requests.get('http://www.google.com/')

# Printando o status code da requisição, e pulando uma linha
print('Status Code:', req_get.status_code, '\n')

# Verifica se o status code é igual a 200
if req_get.status_code == 200:
    # Acessa o corpo da resposta, retornando o html da página em bytes
    html_doc = req_get.content

    # Transformamos o conteúdo html recebido em obj python através do BeautifulSoup, para analisarmos
    soup = BeautifulSoup(html_doc, 'html.parser')

    # Com o 'prettify' podemos exibir o corpo html de forma organizada
    print(soup.prettify())
