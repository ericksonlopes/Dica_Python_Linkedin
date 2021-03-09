from datetime import datetime

method = datetime.now()

currenttime = method.strftime("%H:%M:%S")

print(f'Hora atual: {currenttime}')