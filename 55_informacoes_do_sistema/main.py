import platform

meu_sistema = platform.uname()

print(f"Sistema: {meu_sistema.system}")
print(f"Nome sistema: {meu_sistema.node}")
print(f"Lançamento: {meu_sistema.release}")
print(f"Versão do sistema: {meu_sistema.version}")
print(f"Machine: {meu_sistema.machine}")
print(f"Processador: {meu_sistema.processor}")
