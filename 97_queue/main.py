class Queue(list):
    def __init__(self, *args):
        super().__init__(*args)

    def enqueue(self, item):
        self.append(item)

    def dequeue(self):
        return self.pop(0)

    def is_empty(self):
        return len(self) == 0

    def __repr__(self):
        return f'Queue({super().__repr__()})'

    def __len__(self):
        return super().__len__()

    def __getitem__(self, index):
        return super().__getitem__(index)


if __name__ == '__main__':
    fila = Queue()
    fila.enqueue(1)
    fila.enqueue(2)
    fila.enqueue(3)
    fila.enqueue(4)
    fila.enqueue(5)
    print(fila)
    print(fila.dequeue())
    print(fila)
    print(fila.is_empty())
    print(len(fila))
    print(fila[0])
