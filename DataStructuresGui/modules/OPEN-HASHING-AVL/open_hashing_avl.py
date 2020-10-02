from avl import AvlTree

class OpenHashingAvl:
    def __init__(self, _hash_size=3, _hash_lambda=1):
        self.hash_size = _hash_size
        self.hash_table = []
        self.hash_lambda = _hash_lambda
        for i in range(self.hash_size):
            self.hash_table.append(AvlTree())

    def insert(self, key):
        position = key % self.hash_size
        if self.hash_table[position].root is None:
            self.hash_table[position] = AvlTree([key])
        elif self.hash_table[position].height  < self.hash_lambda:
            self.hash_table[position].insert(key)

    def delete(self, key):
        position = key % self.hash_size
        self.hash_table[position].delete(key)

    def search(self, key):
        position = key % self.hash_size
        if self.hash_table[position].root is not None:
            return self.hash_table[position].find(key)
        else:
            return False

    def balancing_factor(self):
        bfactor = 0
        for tree in self.hash_table:
            if tree.root:
                bfactor += (tree.height + 1)
        bfactor = bfactor / ((self.hash_lambda + 1) * self.hash_size)
        return bfactor
