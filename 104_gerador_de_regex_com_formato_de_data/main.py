import re


def generate_regex_from_date_format(date_format):
    regex = re.escape(date_format)  # Escapa caracteres especiais na string de formato de data
    regex = regex.replace("%Y", r"\d{4}")  # Substitui "%Y" por "\d{4}" para corresponder a quatro dígitos de ano
    regex = regex.replace("%m", r"\d{2}")  # Substitui "%m" por "\d{2}" para corresponder a dois dígitos de mês
    regex = regex.replace("%d", r"\d{2}")  # Substitui "%d" por "\d{2}" para corresponder a dois dígitos de dia

    return regex


data_format = "%Y-%m-%d"

regex_format = generate_regex_from_date_format(data_format)

print(regex_format)
