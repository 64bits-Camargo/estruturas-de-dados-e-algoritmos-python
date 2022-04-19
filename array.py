class Array:

    def __init__(self, size):
        self.size = size
        self.array = [None for _ in range(self.size)]

    def __setitem__(self, index, value):
        count = 0
        while count <= self.size:
            if count == index:
                self.array[count] = value
                return
            count += 1
        raise IndexError

    def __getitem__(self, index):
        count = 0
        while count <= self.size:
            if count == index:
                return self.array[count]
            count += 1
        raise IndexError

    def __delitem__(self, index):
        count = 0
        while count <= self.size:
            if count == index:
                self.array[count] = None
                return
            count += 1
        raise IndexError

    def __repr__(self):
        return str(self.array)


if __name__ == '__main__':
    len_array = 10
    my_array = Array(len_array)

    for i in range(len_array):
        my_array[i] = bin(i*13)

    del my_array[5]
    del my_array[6]
    del my_array[7]

    print(my_array)