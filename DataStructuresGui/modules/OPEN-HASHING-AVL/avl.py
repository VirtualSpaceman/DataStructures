from collections import deque
from graphviz import *
import tempfile
import warnings
warnings.filterwarnings("ignore")
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
class AvlTree:
    def __init__(self, *keys):
        self.root = None
        self.height = -1
        self.tree_dict = dict()
        if len(keys) == 1:
            keys = keys[0]
            for i in keys:
                self.insert(i)

    def bfs(self):
        q = deque()
        if self.root:
            q.append(self.root)
            while len(q):
                node = q.pop()
                if node.key not in self.tree_dict:
                    self.tree_dict[node.key] = []
                    if node.left.root:
                        q.append(node.left.root)
                        self.tree_dict[node.key].append(node.left.root.key)
                    else:
                        self.tree_dict[node.key].append(None)
                    if node.right.root:
                        q.append(node.right.root)
                        self.tree_dict[node.key].append(node.right.root.key)
                    else:
                        self.tree_dict[node.key].append(None)



    def dfs(self, tree_root):

        if tree_root and (tree_root.key not in self.tree_dict):
            self.tree_dict[tree_root.key] = []

            if tree_root.left.root:
                self.tree_dict[tree_root.key].append(tuple([tree_root.left.root.key,
                                                           tree_root.left.height]))
            else:
                self.tree_dict[tree_root.key].append(tuple([None, -1]))
            if tree_root.right.root:
                self.tree_dict[tree_root.key].append(tuple([tree_root.right.root.key,
                                                     tree_root.right.height]))
            else:
                self.tree_dict[tree_root.key].append(tuple([None, -1]))
            self.dfs(tree_root.left.root), self.dfs(tree_root.right.root)

    def bfs_insertion(self, sub_avl):
        q = deque()
        q.append(self.root)
        while len(q):
            node = q.pop()
            sub_avl.insert(node.key)
            if node.left.root:
                q.append(node.left.root)
            if node.right.root:
                q.append(node.right.root)

    def show(self, operation):
        self.tree_dict = dict()
        # self.dfs(self.root)
        self.bfs()
        avl = Digraph( format='png', node_attr={'shape': 'record', 'height': '.2'})
        avl.attr(label = operation)
        null_count = 0
        for k in self.tree_dict:
            avl.node(str(k), '<f0> |<f1> ' + str(k) + '|<f2> ')
            if self.tree_dict[k][0] is not None:
                avl.node(str(self.tree_dict[k][0]), '<f0> |<f1> ' + str(self.tree_dict[k][0]) + '|<f2> ')
                avl.edge(str(k) + ':f0', str(self.tree_dict[k][0]) + ':f1')
            else:
                avl.node('null' + str(null_count), shape='point')
                avl.edge(str(k) + ':f0', 'null' + str(null_count))
                null_count += 1
            if self.tree_dict[k][1] is not None:
                avl.node(str(self.tree_dict[k][1]), '<f0> |<f1> ' + str(self.tree_dict[k][1]) + '|<f2> ')
                avl.edge(str(k) + ':f2', str(self.tree_dict[k][1]) + ':f1')
            else:
                avl.node('null' + str(null_count), shape='point')
                avl.edge(str(k) + ':f2', 'null' + str(null_count))
                null_count += 1

        avl.render(view=True)

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            self.root.left = AvlTree()
            self.root.right = AvlTree()

        elif key < self.root.key:
            self.root.left.insert(key)
        elif key > self.root.key:
            self.root.right.insert(key)
        self.set_height()
        self.balance()

    def delete(self, key):
        if self.root:
            if self.root.key == key:
                if self.height == 0:
                    self.__dict__.update(AvlTree().__dict__)
                else:
                    left_tree = self.root.left
                    right_tree = self.root.right
                    if right_tree.root and left_tree.root:
                        if left_tree.height >= right_tree.height:
                            left_tree.bfs_insertion(right_tree)
                            self.__dict__.update(right_tree.__dict__)
                        else:
                            right_tree.bfs_insertion(left_tree)
                            self.__dict__.update(left_tree.__dict__)
                    elif right_tree.root:
                        self.__dict__.update(right_tree.__dict__)
                    elif left_tree.root:
                        self.__dict__.update(left_tree.__dict__)

            elif key < self.root.key:
                self.root.left.delete(key)
            else:
                self.root.right.delete(key)
        if self.root:
            self.set_height()
            self.balance()
    def find(self, key):
        aux = self
        while aux.root:
            if aux.root.key == key:
                print('The key ' + str(key) + ' was found')
                return True
            elif key < aux.root.key:
                aux = aux.root.left
            else:
                aux = aux.root.right
        print('The key ' + str(key) + ' was not found')
        return False



    def set_height(self):
        self.height = max(self.root.left.height, self.root.right.height) + 1

    def update_heights(self, recurse=True):
        if self.root:
            if recurse:
                if self.root.left:
                    self.root.left.update_heights()
                if self.root.right:
                    self.root.right.update_heights()
            self.set_height()
        else:
            self.height = -1

    def delta_h(self):
        return (self.root.left.height - self.root.right.height)

    def simple_left_right_rotation(self):
        X = self.root.left.root
        Y = X.right.root
        Z = self.root
        self.root = X
        Z.left.root = Y
        X.right.root = Z
        self.update_heights()

    def simple_right_left_rotation(self):
        X = self.root.right.root
        Y = X.left.root
        Z = self.root

        self.root = X
        Z.right.root = Y
        X.left.root = Z
        self.update_heights()

    def double_left_right_rotation(self):
        X = self.root.left.root.right.root
        Y = X.left.root
        Z = self.root.left.root
        self.root.left.root = X
        Z.right.root = Y
        X.left.root = Z

        self.root.left.update_heights()

        X = self.root.left.root
        Y = X.right.root
        Z = self.root
        self.root = X
        Z.left.root = Y
        X.right.root = Z

        self.update_heights()

    def double_right_left_rotation(self):
        X =self.root.right.root.left.root
        Y = X.right.root
        Z = self.root.right.root
        self.root.right.root = X
        Z.left.root = Y
        X.right.root = Z

        self.root.right.update_heights()

        X = self.root.right.root
        Y = X.left.root
        Z = self.root
        self.root = X
        Z.right.root = Y
        X.left.root = Z

        self.update_heights()

    def balance(self):
        self.update_heights(False)
        while self.delta_h() < -1 or self.delta_h() > 1:
            if self.delta_h() < -1:
                if self.root.right.delta_h() > 0:
                    self.double_right_left_rotation()
                else:
                    self.simple_right_left_rotation()
            elif self.delta_h() > 1:
                if self.root.left.delta_h() < 0:
                    self.double_left_right_rotation()
                else:
                    self.simple_left_right_rotation()
