from avl import AvlTree
from collections import deque

class LambdaHMA:
    def __init__(self, _hash_size=3, _hash_lambda=1):
        self.hash_size = _hash_size
        self.hash_table = []
        self.full_cells = 0
        self.rehashed = False
        for i in range(self.hash_size):
            self.hash_table.append(AvlTree())
        self.hash_lambda = _hash_lambda
        self.next_prime = lambda n,k=1,m=1:m%k*k>n or-~self.next_prime(n,k+1,m*k*k)

    def insert(self, key):
        tries = 0
        inserted = False
        self.rehashed = False
        if self.full_cells > (self.hash_size // 2):
            print('rehashing - values', key)
            self.rehashing()
            self.full_cells = 0
            self.rehashed = True
        last_position = -1
        while not inserted:
            position = (key + tries ** 2) % self.hash_size
            if not self.hash_table[position].find(key):
                self.hash_table[position].insert(key)
                last_position = position
                if self.hash_table[position].height > self.hash_lambda:
                    self.hash_table[position].delete(key)
                else:
                    inserted = True
            tries += 1

        self.full_cells = self.number_of_full_cells()
        # print(self.full_cells)


    def rehashing(self):
        new_hash_size = self.next_prime(2 * self.hash_size)
        print('New prime', new_hash_size)
        aux_table = self.hash_table[:]
        self.hash_table = []
        for i in range(new_hash_size):
            self.hash_table.append(AvlTree())
        self.hash_size = new_hash_size
        q = deque()
        for tree in aux_table:
            if tree.root:
                while tree.root:
                    key = tree.root.key
                    q.append(key)
                    tree.delete(key)
        print('Inserting keys in new hash table')
        while len(q):
            key = q.pop()
            self.insert(key)


    def delete(self, key):
        for tries in range(self.hash_size + 1):
            position = (key + tries ** 2) % self.hash_size
            if self.hash_table[position].root is not None:
                if self.hash_table[position].find(key):
                    self.hash_table[position].delete(key)
                    print('The key was deleted', key)
                    return True
        print('The key was not found', key)
        print('Cannot delete')
        return False

    def find(self, key):
        for tries in range(self.hash_size + 1):
            position = (key + tries ** 2) % self.hash_size
            if self.hash_table[position].root is not None:
                if self.hash_table[position].find(key):
                    print('The key was found', key)
                    return True
        print('The key was not found', key)
        return False

    def number_of_full_cells(self):
        fcells = 0
        for tree in self.hash_table:
            if tree.root:
                if (tree.height ) == self.hash_lambda:
                    fcells += 1
        return fcells

    # def full_cells_rate(self):
    #     return self.number_of_full_cells() / self.hash_size

    def balancing_factor(self):
        bfactor = 0
        for tree in self.hash_table:
            if tree.root:
                bfactor += (tree.height + 1)
        bfactor = bfactor / ((self.hash_lambda + 1) * self.hash_size)
        return bfactor
