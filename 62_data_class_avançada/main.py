from dataclasses import dataclass


@dataclass
class Carro:
    modelo: str
    ano: int

    def __init__(self, modelo: str, ano: int = 1885):
        self.modelo = modelo
        self.ano = ano

    def __repr__(self):
        return f"A instância da classe {self.__class__.__name__} tem como modelo um {self.modelo} do ano {self.ano}"


if __name__ == '__main__':
    fusca = Carro('Fusca', 1995)

    print(fusca.modelo)
    # Fusca
    print(fusca.ano)
    # 1995
    print(fusca)
    # A instância da classe Carro tem como modelo um Fusca do ano 1995
