# Instalar biblioteca
# pip install requests
# pip install beautifulsoup4

# importando as bibliotecas
import requests
from bs4 import BeautifulSoup

# Realiza uma requizição do tipo get na url indicada
req_get = requests.get('https://github.com')

# Printando o status code da requisição
print('Status Code:', req_get.status_code)

# Verifica se o status code é igual a 200
if req_get.status_code == 200:
    soup = BeautifulSoup(req_get.content, 'html.parser')
    print(soup.prettify())
