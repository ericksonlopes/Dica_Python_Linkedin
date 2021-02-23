import socket

# Host
host = 'google.com'

# Recebendo IP do host
ip = socket.gethostbyname(host)

# Exibir resultado
print(f"O IP do Host '{host}' é : {ip}")
# Saida: O IP do Host 'google.com' é : 216.58.202.142
