#ifndef HASH_FECHADA_HPP
#define HASH_FECHADA_HPP
#include <vector>
#include <iostream>

class hash_fechada
{
public:
    hash_fechada(int TH, int tentativa);
    void inserir(int valor);
    void deletar(int valor);
    void print();
    double balance_factor();

private:
    int LINEAR = 1;
    int QUADRATICA = 2;
    int DUPLO_HASHING = 3;
    bool empty();
    int TH;
    int tentativa;
    std::vector<int> hash_table;
    int prox_menor_primo(int numero);


};

#endif // HASH_FECHADA_HPP
