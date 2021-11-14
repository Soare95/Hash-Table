class HashTable:

    def __init__(self, size):
        self.size = size
        self.hashmap = [[] for i in range(self.size)]

    def __str__(self):
        return str(self.__dict__)

    def _hash(self, key):
        hash = 0
        for i in key:
            hash = (hash + ord(i)) % self.size
        return hash

    def set(self, key, value):
        hash_value = self._hash(key)
        reference = self.hashmap[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                reference[i][0] = value
        reference.append([key, value])

    def get(self, key):
        hash_value = self._hash(key)
        reference = self.hashmap[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                return reference[i][1]

    def keys(self):
        dict_keys = []
        for i in range(len(self.hashmap)):
            if self.hashmap[i]:
                dict_keys.append(self.hashmap[i][0][0])
        return dict_keys

    def values(self):
        dict_values = []
        for i in range(len(self.hashmap)):
            if self.hashmap[i]:
                dict_values.append(self.hashmap[i][0][1])
        return dict_values

my_hash = HashTable(20)
my_hash.set("Grapes", 1000)
my_hash.set("Apples", 32)
my_hash.set("Banana", 50)
print(my_hash.get("lala"))
print(my_hash.keys())
print(my_hash.values())
print(my_hash)
