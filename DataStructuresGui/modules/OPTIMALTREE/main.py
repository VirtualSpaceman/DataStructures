from optimaltree import OptimalTree

def main():
    f = [1, 3, 2]
    k = [0, 70, 60]
    ot = OptimalTree(k, f)

    ot.create_matrix()
    ot.build()
    ot.find(70)
    ot.show('')


if __name__ == '__main__':
    main()
