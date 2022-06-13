from datetime import date
from rich import print
today = date.today()

# Para clientes
print(str(today))
# 2022-06-13

# Para devs
print(repr(today))
print(locals())
# datetime.date(2022, 6, 13)

