import random
import string

# Recebe Dois alfabetos um com letras minusculas e outro com letras maiusculas
letters = string.ascii_letters
# Recebe numeros de 1 a 9
number = string.digits
# Recebe puntuação
punctuation = string.punctuation

# Concatenando todos os caracteres
all_carac = letters + number + punctuation

# Definindo quantidade de caracteres
lenght = 16

# Concatena uma lista de strings recebida pelo sample
password = "".join(random.sample(all_carac, lenght))

print(password)
# Saida :
# gB}|x:fbCqFn'Wwa
# vn{pD(r+O?]s6&J'
# ^n3<XUPa&6Yk{0_g
