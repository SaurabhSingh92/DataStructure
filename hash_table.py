class HashTable():

    def __init__(self, size):
        self.data_list = [None] * size

    def get_index(self, str):
        result = 0
        for ch in str:
            result += ord(ch)
        return result % len(self.data_list)

    def insert(self, key, val):
        idx = HashTable.get_index(self, key)
        self.data_list[idx] = (key, val)

    def list(self):
        return [kv[0] for kv in self.data_list if kv is not None]

    def find(self, key):
        idx = HashTable.get_index(self, key)
        return self.data_list[idx]

    def update(self, key, val):
        idx = HashTable.get_index(self, key)
        self.data_list[idx] = (key, val)

    def __repr__(self):
        for kv in self.data_list:
            if kv is not None:
                print(f"{kv[0]} : {kv[1]}")
        return ''

if __name__ == "__main__":
    t = HashTable(100)
    t.insert("abc", 1)
    t.insert("xyz", 10)
    t.insert("pqr", 100)
    print(t.list())
    print(t.find("abc"))
    t.update("abc", 99)
    print(t)

    print(t.get_index("abc"))
    print(t.get_index("cba"))
