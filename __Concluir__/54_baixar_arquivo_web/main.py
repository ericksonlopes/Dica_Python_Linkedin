import requests


def baixar_arquivo(url: str, endereco: str):
    """Baixa arquivos publicos em links na internet em uma pasta.
    :param url: Link http ou https do arquivo na internet.
    :type url: String
    :param endereco: caminho da pasta que vai receber o arquivo.
    :type endereco: String
    """
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
    else:
        resposta.raise_for_status()


file_to_dowload = "https://www.linkedin.com/favicon.ico"
path = 'image.ico'
baixar_arquivo(file_to_dowload, path)

