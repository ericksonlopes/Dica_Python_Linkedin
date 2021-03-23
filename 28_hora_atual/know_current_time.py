from datetime import datetime

# instanciando obj com os dados do dia atual
method = datetime.now()

# formatando o obj para uma string
currenttime = method.strftime("%H:%M:%S")

print(f'Hora atual: {currenttime}')
# Hora atual: 07:33:45
