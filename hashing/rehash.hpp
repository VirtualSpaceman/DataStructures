#ifndef REHASH_HPP
#define REHASH_HPP
#include <vector>
#include <iostream>

class reHash
{
public:
    reHash(int TH);
    void inserir(int valor);
    void deletar(int valor);
    bool empty();
    double full();
    void print();
    int num_elementos;
private:
    int TH;
    std::vector<int> hash;
    double cheia();
    int primo_mais_prox(int numero);
    void rehashing();
    double HASH_CHEIA = 0.5;
};

#endif // REHASH_HPP
