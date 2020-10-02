import math
from graphviz import *
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class OptimalTree:
    def __init__(self, _keys=[], _freq=[]):
        self.root = None
        self.cost_matrix = None
        self.tree_matrix = None
        self.total_cost = None
        self.keys = _keys.copy()
        self.freq = _freq.copy()
        # cria uma lista de tuplas key, freq
        self.data = list(zip(self.keys, self.freq))
        # ordena a lista de tuplas para poder fazer a arvore
        self.data.sort()


    # calcula a soma das frequencias em um intervalo
    def fsum(self, a, b):
        s = 0
        for i in range(a, b + 1):
            s += self.data[i][1]
        return s
    # cria a matriz de custo utilizando programacao dinamica
    # nao recalculando subcasos e os aproveitando
    def create_matrix(self):
        if len(self.keys) != len(self.freq):
            return
        n = len(self.data)
        self.cost_matrix = [[None for i in range(n)] for j in range(n)]
        self.tree_matrix = [[None for i in range(n)] for j in range(n)]
        # caso base
        # preenche a diagonal da matriz de custo com o valor da frequencia
        # da chave, visto que o custo para a propria chave eh a propria frequencia

        for i in range(n):
            self.cost_matrix[i][i] = self.data[i][1]
            self.tree_matrix[i][i] = self.data[i][0], i
        # calcula o custo de uma subarvore baseado no custo de suas arvores filhas
        # so é necessario calcular da diagonal para cima
        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1
                self.cost_matrix[i][j] = math.inf
                for r in range(i, j + 1):
                    # custo do elemento com chave[r] = min(custo[i][r - 1], custo[j][r + 1] + soma(de i a j,freq[i])
                    cost = (self.cost_matrix[i][r - 1] if r > i else 0) + \
                        (self.cost_matrix[r + 1][j] if r < j else 0) + \
                         self.fsum(i, j)
                    # cost eh atualizado para o menor custo
                    # e adiciona-se o chave de menor custo a matriz de vertices e o seu valor
                    if cost < self.cost_matrix[i][j]:
                        self.cost_matrix[i][j] = cost
                        self.tree_matrix[i][j] = self.data[r][0], r

        # o custo da arvore otima
        self.total_cost = self.cost_matrix[0][n - 1]

    # monta a arvore otima com base na matriz de vertice ja calculada
    def build_tree(self, node, pos_i, pos_j):
        n = len(self.data)
        if n == 0:
            return
        v = self.tree_matrix[pos_i][pos_j]
        if pos_i > pos_j:
            return None
        node = Node(v[0])
        if v[1] > 0:
            node.left = self.build_tree(node.left, pos_i, v[1] - 1)
        if v[1] + 1 < n:
            node.right = self.build_tree(node.right, v[1] + 1, pos_j)
        return node

    # funcao que visita todos os vertices para montar um grafo
    # no graphviz
    def show(self, operation):
        from collections import deque
        q = deque()
        opt_tree = Digraph( format='png', node_attr={'shape': 'record', 'height': '.2'})
        opt_tree.attr(label = operation)
        null_count = 0
        q.append(self.root)
        while len(q):
            node = q.pop()
            if node:
                opt_tree.node(str(node.key), '<f0> |<f1> ' + str(node.key) + '|<f2> ')
                if node.left:
                    opt_tree.node(str(node.left.key), '<f0> |<f1> ' + str(node.left.key) + '|<f2> ')
                    opt_tree.edge(str(node.key) + ':f0', str(node.left.key) + ':f1')
                    q.append(node.left)
                else:
                    opt_tree.node('null' + str(null_count), shape='point')
                    opt_tree.edge(str(node.key) + ':f0', 'null' + str(null_count))
                    null_count += 1
                if node.right:
                    opt_tree.node(str(node.right.key), '<f0> |<f1> ' + str(node.right.key) + '|<f2> ')
                    opt_tree.edge(str(node.key) + ':f2', str(node.right.key) + ':f1')
                    q.append(node.right)
                else:
                    opt_tree.node('null' + str(null_count), shape='point')
                    opt_tree.edge(str(node.key) + ':f2', 'null' + str(null_count))
                    null_count += 1
        opt_tree.render(filename='optimal_graph', view=False, directory='./modules/OPTIMALTREE/graphviz_optimal')

    # chama a funcao build_tree e constroi toda a arvore
    def build(self):
        self.create_matrix()
        n = len(self.data)
        self.root = self.build_tree(self.root, 0, n - 1)

    # busca em uma arvore binaria
    def find(self, key):
        aux = self.root
        while aux:
            if aux.key == key:
                print('The key ' + str(key) + ' was found')
                return True
            elif key < aux.key:
                aux = aux.left
            else:
                aux = aux.right
        print('The key ' + str(key) + ' was not found')
        return False
