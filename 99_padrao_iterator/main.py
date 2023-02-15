class MyIterator:
    def __init__(self, data):
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        result = self.data[self.index]
        self.index += 1
        return result


if __name__ == '__main__':
    my_iterator = MyIterator([1, 2, 3, 4, 5])

    for item in my_iterator:
        print(item)
