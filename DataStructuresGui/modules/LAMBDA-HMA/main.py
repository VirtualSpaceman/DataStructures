from lambda_hma import LambdaHMA
from random import randint
from avl import AvlTree

import sys
import time
import warnings

def main():
    warnings.filterwarnings("ignore")
    #th, lambda
    h = LambdaHMA(5, 3)
    S = [22, 43, 36, 16, 44, 77, 62, 32, 71, 31, 41, 27, 29, 19, 7, 14, 91, 81, 1]


    for key in S:
        # print(key)
        h.insert(key)
    # print('passei')
    h.delete(1)
    h.delete(85)
    print(h.balancing_factor())
    # print(h.hash_size)

    c = 0
    for tree in h.hash_table:
        if tree:
            tree.show(str(c))
            time.sleep(3)
        c += 1
    # print(avl_hashing.balancing_factor())
    # avl_hashing.search(33)
if __name__ == '__main__':
    main()
