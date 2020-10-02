from avl import AvlTree
import pprint
from PyQt5 import QtCore, QtGui, QtWidgets

def main():
    a = AvlTree([0,1, 2, 6])
    pp = pprint.PrettyPrinter(indent=4)
    a.bfs()
    # a.dfs(a.root)
    a.show('')
    pp.pprint(a.tree_dict)

if __name__ == '__main__':
    main()
