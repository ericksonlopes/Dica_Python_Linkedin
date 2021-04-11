import json

dados_json = '{"name": "Erickson", "age": 19, "city": "São Paulo"}'

carregar_dados = json.loads(dados_json)

print(carregar_dados['name'])
# Erickson

print(carregar_dados['age'])
# 19