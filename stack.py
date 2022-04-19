class Stack:

    def __init__(self):
        self.items = []
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, value):
        count = 0
        if self.size is None:
            self.items = self.items + [value]
            self.size += 1
        else:
            while count <= self.size:
                if count == self.size:
                    self.items = self.items + [value]
                    self.size += 1
                    return
                count += 1

    def pop(self):
        count = 0
        while count <= self.size:
            if count == self.size:
                del self.items[count - 1]
                self.size -= 1
                return
            count += 1

    def is_empty(self):
        return self.size is None


if __name__ == '__main__':
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)


    stack.pop()
    print(stack.items)
    print(len(stack))