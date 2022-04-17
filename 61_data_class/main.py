from dataclasses import dataclass


@dataclass
class Carro:
    modelo: str
    ano: int


if __name__ == '__main__':
    fusca = Carro('Fusca', 1995)

    print(fusca.modelo)
    print(fusca.ano)
