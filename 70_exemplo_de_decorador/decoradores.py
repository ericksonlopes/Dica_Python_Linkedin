def decorador(func):
    def exibe_uma_mensagem(*args, **kwargs):
        print(f"chamando a função: func.__name__")
        return func(*args, **kwargs)

    return exibe_uma_mensagem


@decorador
def dobro(x):
    return x * 2


print(dobro(10))
# Chamando funcao: dobro()
# 20
