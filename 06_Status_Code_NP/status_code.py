# Instalar biblioteca
# pip install requests

# importando biblioteca
import requests

# Realiza uma requizição do tipo get na url indicada
req_get = requests.get('https://www.google.com')

# Printando o resultado
print(req_get.status_code)
