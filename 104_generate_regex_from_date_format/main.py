import re


def generate_regex_from_date_format(date_format):
    regex = re.escape(date_format)

    regex = regex.replace("%Y", r"\d{4}")
    regex = regex.replace("%m", r"\d{2}")
    regex = regex.replace("%d", r"\d{2}")
    regex = regex.replace("%H", r"\d{2}")
    regex = regex.replace("%M", r"\d{2}")
    regex = regex.replace("%S", r"\d{2}")

    return regex


data_format = "%Y-%m-%d"

regex_format = generate_regex_from_date_format(data_format)

print(regex_format)
