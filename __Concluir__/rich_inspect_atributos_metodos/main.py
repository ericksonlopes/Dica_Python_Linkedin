from rich import inspect

# Se você quiser ver rapidamente quais atributos e métodos de um objeto Python estão disponíveis,
# use o método de inspeção do Rich.
# o método de inspeção de Rich permite criar um belo relatório para qualquer objeto Python,
# incluindo uma sequência.

inspect('ola mundo', methods=True)
