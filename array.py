class Array:

    def __init__(self, size):
        self.item_count = 0
        self.size = size
        self.array = [None for _ in range(self.size)]

    def __len__(self):
        return self.item_count

    def __getitem__(self, index):
        pass

    def __delitem__(self, index):
        pass
