def echo_funcname(func):
    def finterna(*args, **kwargs):
        print("Chamando funcao: %s()" % (func.__name__))
        return func(*args, **kwargs)

    return finterna


@echo_funcname
def dobro(x):
    return x * 2


dobro(10)