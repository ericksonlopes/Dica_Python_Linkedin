# pip install google_currency

from google_currency import convert

# Converter dolar(USD) para Reais(BRL)
data = convert('usd', 'brl', 1)

print(data)
# {"from": "USD", "to": "BRL", "amount": "4.80", "converted": true}


# Converter Euro(EUR) para Reais(BRL)
data = convert('eur', 'brl', 1)

print(data)
# {"from": "EUR", "to": "BRL", "amount": "5.19", "converted": true}
