from open_hashing_avl import OpenHashingAvl
from random import randint

import sys
import time
import warnings

def main():
    warnings.filterwarnings("ignore")
    avl_hashing = OpenHashingAvl(7, 1)
    S = [0, 1, 85, 6, 36, 46, 89, 112, 44]
    for key in S:
        avl_hashing.insert(key)

    c = 0
    for tree in avl_hashing.hash_table:
        if tree:
            tree.show(str(c))
        time.sleep(1)
        c += 1
        print(avl_hashing.balancing_factor())
    avl_hashing.search(36)
if __name__ == '__main__':
    main()
