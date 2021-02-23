import socket

# Host
host = 'google.com'

# Recebendo IP do host
ip = socket.gethostbyname(host)

# Exibir resultado
print(f"O IP do Host '{host}' é : {ip}")
