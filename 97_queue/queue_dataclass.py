from dataclasses import dataclass


@dataclass
class Item:
    name: str
    age: int


@dataclass
class Queue(list):
    def enqueue(self, item: Item):
        self.append(item)

    def dequeue(self) -> Item:
        return self.pop(0)

    def __repr__(self):
        return f"{self.__class__.__name__}({super().__repr__()})"


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(Item("A", 1))
    queue.enqueue(Item("B", 2))
    queue.enqueue(Item("C", 3))
    print(queue)
    print(queue.dequeue())
    print(queue)
