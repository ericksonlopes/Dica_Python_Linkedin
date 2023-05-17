import re

data_format = "%Y-%m-%d"
regex = re.escape(data_format)  # Escapa caracteres especiais na string de formato de data
regex = re.sub(r"%Y", r"\d{4}", regex)  # Substitui "%Y" por "\d{4}" para corresponder a quatro dígitos de ano
regex = re.sub(r"%m", r"\d{2}", regex)  # Substitui "%m" por "\d{2}" para corresponder a dois dígitos de mês
regex = re.sub(r"%d", r"\d{2}", regex)  # Substitui "%d" por "\d{2}" para corresponder a dois dígitos de dia


"""
O código acima utiliza a biblioteca padrão do Python "re" (expressões regulares) para construir uma expressão regular
(regex) a partir de uma string de formato de data. A string de formato de data utilizada é "%Y-%m-%d", que representa o
ano, mês e dia separados por hífens.

O resultado final é uma expressão regular que corresponde à data no formato "YYYY-MM-DD". Essa expressão regular pode 
ser usada para validar datas em strings ou para extrair datas de textos usando a função re.search() ou re.findall().
"""
