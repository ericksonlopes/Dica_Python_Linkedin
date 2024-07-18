import queue
import threading
import time

# Criando uma queue
q = queue.Queue()


# Função para processar itens da queue
def process_queue():
    while True:
        item = q.get()
        if item is None:
            break
        print(f'Processando {item}')
        time.sleep(1)
        q.task_done()


# Criando e iniciando uma thread para processar a queue
thread = threading.Thread(target=process_queue)
thread.start()

# Adicionando itens à queue
for item in range(5):
    q.put(item)

# Esperando todos os itens serem processados
q.join()

# Enviando sinal para finalizar a thread
q.put(None)
thread.join()
