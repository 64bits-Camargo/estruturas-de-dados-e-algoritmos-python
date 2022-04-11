import json

class DuplicateKeyError(Exception):

    def __init__(self, key):
        self.message = "Error adding key, duplicate key '{key}'".format(key=key)
        super().__init__(self.message)


class HashTable:
    
    def __init__(self, size=10):
        self.size = size
        self.table =[[] for _ in range(self.size)]
    
    def hashing(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        hash_key = self.hashing(key)

        if self.table[hash_key]:
            for index, k_value in enumerate(self.table[hash_key]):
                k, v = k_value

                if key == k:
                    raise DuplicateKeyError(key)

        self.table[hash_key].append((key, value))

    def __repr__(self):
        return 'HashTable(table={result})'.format(result=json.dumps(self.table))

if __name__ == '__main__':
    hash_table = HashTable()

    print(hash_table)


    hash_table.insert('Nome', 'Mateus 1')
    # hash_table.insert('Nome', 'Mateus 1') 
    hash_table.insert('Noma', 'Mateus 2') 
    hash_table.insert('Nomi', 'Mateus 3')
    hash_table.insert('Nomo', 'Mateus 4')
    hash_table.insert('Nom2', 'Mateus 5')
    hash_table.insert('No2m2', 'Mateus 6')
    hash_table.insert('No2m322', 'Mateus 326')
    hash_table.insert('No2m323322', 'Mate3232us 326')
    hash_table.insert('No32322m323322', 'Mate3232us 326')
    hash_table.insert('3232322', 'Mate3232us 326')

    hash_table.insert('3232DSDS322', 'Mate3DSSD232us 326')

    print(hash_table)
