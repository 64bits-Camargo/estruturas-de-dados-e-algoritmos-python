import json
from math import pi


class DuplicateKeyError(Exception):

    def __init__(self, key):
        self.message = "Error adding key, duplicate key '{key}'".format(key=key)
        super().__init__(self.message)


class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.tables = [[] for _ in range(self.size)]

    def hashing(self, key):
        return hash(key) % self.size

    def __setitem__(self, key, value):
        hash_key = self.hashing(key)
        if self.tables[hash_key]:
            for _, k_value in enumerate(self.tables[hash_key]):
                k, v = k_value
                if key == k:
                    self.tables[hash_key][_] = (key, value)
                    break
        self.tables[hash_key].append((key, value))

    def __getitem__(self, key):
        hash_key = self.hashing(key)
        if self.tables[hash_key]:
            for _, k_value in enumerate(self.tables[hash_key]):
                k, v = k_value
                if key == k:
                    return v

    def __delitem__(self, key):
        hash_key = self.hashing(key)
        if self.tables[hash_key]:
            for _, k_value in enumerate(self.tables[hash_key]):
                k, v = k_value
                if key == k:
                    del self.tables[hash_key][_]
                    return
        raise KeyError

    def __repr__(self):
        return 'HashTable(table={result})'. \
            format(result=json.dumps(self.tables, indent=2))


if __name__ == '__main__':
    hash_table = HashTable()

    for i in range(100):
        hash_table[i] = round(i * pi, 2)

    for index, table in enumerate(hash_table.tables):
        print("Table {index} -> {table}".format(index=index + 1, table=table))
