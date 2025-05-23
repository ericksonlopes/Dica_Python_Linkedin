from fastmcp import FastMCP

server = FastMCP("Servidor de Teste")
server.dependencies = []


@server.tool()
def somar(a: int, b: int) -> int:
    """Soma dois números inteiros. Exemplo: '8 10'"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Os parâmetros devem ser números inteiros.")

    return a + b


if __name__ == "__main__":
    server.run()
