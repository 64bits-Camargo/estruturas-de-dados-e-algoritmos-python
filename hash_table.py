class HashTable:
    
    def __init__(self, size=10):
        self.table = [None] * size


    def hashing(self, key):
        return key % self.size
    
    def insert(self, key, value):
        hash_key = hashing(key)
        self.table[hash_key] = value

    

