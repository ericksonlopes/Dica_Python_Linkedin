import json


def mapear_json(json_data):
    mapeamento = {}

    def percorrer_json(data, path=""):
        if isinstance(data, dict):
            for key, value in data.items():
                new_path = f"{path}.{key}" if path else key
                percorrer_json(value, new_path)

        elif isinstance(data, list):
            for index, item in enumerate(data):
                new_path = f"{path}[{index}]"
                percorrer_json(item, new_path)

        else:
            mapeamento[path] = data

    percorrer_json(json_data)
    return mapeamento


# Exemplo de JSON
json_string = '''
{ 
    "nome": "John Doe",
    "idade": 30, 
    "endereco": {
        "rua": "Rua Principal",
        "cidade": "Exemplo City"
    },
    "telefones": [
        "123456789",
        "987654321"
    ]
}
'''

# Carrega o JSON
data_json = json.loads(json_string)

# Gera o mapeamento
mapeamento_json = mapear_json(data_json)

# Imprime o mapeamento
for k, v in mapeamento_json.items():
    print(f"{k}: {v}")
