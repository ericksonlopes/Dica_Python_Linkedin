import xml.etree.ElementTree as ET


def mapear_xml(xml_data):
    mapeamento = {}

    def percorrer_xml(elemento, path=""):
        novo_path = path + "." + elemento.tag if path else elemento.tag

        if elemento.text:
            mapeamento[novo_path] = elemento.text

        for child in elemento:
            percorrer_xml(child, novo_path)

    root = ET.fromstring(xml_data)

    percorrer_xml(root)
    return mapeamento


# Exemplo de XML
xml_string = '''
<root>
    <nome>John Doe</nome>
    <idade>30</idade>
    <endereco>
        <rua>Rua Principal</rua>
        <cidade>Exemplo City</cidade>
    </endereco>
    <telefones>
        <telefone>123456789</telefone>
        <telefone>987654321</telefone>
    </telefones>
</root>
'''

# Gera o mapeamento
mapeamento_xml = mapear_xml(xml_string)

# Imprime o mapeamento
for key, value in mapeamento_xml.items():
    print(f"{key}: {value}")
