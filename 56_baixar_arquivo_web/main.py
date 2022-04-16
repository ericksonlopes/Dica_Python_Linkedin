# pip install requests
import requests


def baixar_arquivo(url: str, endereco: str) -> None:
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


# link do arquivo que deseja baixar
file_url = "https://www.linkedin.com/favicon.ico"

# nome que sera salvo
name_file = 'image.ico'

# executa função que realiza download
baixar_arquivo(file_url, name_file)
