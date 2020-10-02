#include <iostream>
#include "node.hpp"
#include "splaytree.hpp"

using namespace std;

int main()
{
    splaytree *splay = new splaytree();
    std::vector<int> S = {81 ,1, 4, 1, 81, 16, 7, 3, 58, 32, 21, 4, 9};
    std::vector<int> B = {4, 9, 81, 1, 11, 14, 4, 1};
    std::vector<int> D = {1, 3, 32, 16};

    for(int i = 0; i < S.size(); i++)
    {
        std::cout << "PASSO " << i+1 << ", INSERIR ELEMENTO " << S[i] << '\n';
        splay->insert(splay->root, S[i]);
        splay->print(splay->root, 0);
        cout << '\n';
    }

    cout << "================BUSCA=============\n";
    for(int i = 0; i < B.size(); i++)
    {
        std::cout << "PASSO " << i+1 << ", BUSCAR ELEMENTO " << B[i] << '\n';
        splay->find(splay->root, B[i]);
        splay->print(splay->root, 0);
        cout << '\n';
    }

    cout << "================DELECAO=============\n";
    for(int i = 0; i < D.size(); i++)
    {
        std::cout << "PASSO " << i+1 << ", DELETAR ELEMENTO " << D[i] << '\n';
        splay->remove(splay->root, D[i]);
        splay->print(splay->root, 0);
        cout << '\n';
    }
    return 0;
}
