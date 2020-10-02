#include "hash_fechada.hpp"

hash_fechada::hash_fechada(int TH, int tentativa)
{
    this->TH = TH;
    this->tentativa = tentativa;
    this->hash_table.resize(TH);
    std::fill(this->hash_table.begin(), this->hash_table.end(), -1);

}

void hash_fechada::inserir(int valor)
{
    int TH_aux = this->TH, posicao;
    for(int i = 0; i < this->TH; i++)
    {
        if(this->tentativa == LINEAR)
        {
            posicao = (valor + i)% this->TH;
            if(i == 0)
            {
                std::cout << "Elemento para inserir " << valor << '\n';
                std::cout << "\t" << valor << " MOD " << this->TH << " = " << posicao << '\n';
            }
            else
                std::cout << "\t" << valor << '+' << i << " MOD " << this->TH << " = " << posicao << '\n';

        }
        else if(this->tentativa == QUADRATICA)
        {
            posicao = (valor + i*i)% this->TH;
            if(this->num_elementos > this->TH/2 + 1){
                std::cout << "Hash cheia, pois a tabela ja esta metade cheia\n";
                return;
            }
            if(i == 0)
            {
                std::cout << "Elemento para inserir " << valor << '\n';
                std::cout << "\t" << valor << " MOD " << this->TH << " = " << posicao << '\n';
            }
            else
                std::cout << "\t" << valor << '+' << i << "^2 MOD " << this->TH << " = " << posicao << '\n';
        }
        else if(this->tentativa == DUPLO_HASHING)
        {
            posicao = valor % TH_aux;
            if(i == 0)
            {
                std::cout << "Elemento para inserir " << valor << '\n';
                std::cout << "\tTH(" << i << ")=" << TH_aux << ",\t" << valor <<
                             " MOD " << TH_aux << " = " << posicao << '\n';
            }
            else
                std::cout << "\tTH(" << i << ")=" << TH_aux << ",\t" << valor <<
                             " MOD " << TH_aux << " = " << posicao << '\n';

            TH_aux = prox_menor_primo(TH_aux);
        }

        if(hash_table[posicao] == -1)
        {
            hash_table[posicao] = valor;
            std::cout << "\tElemento " << valor << " inserido no indice " << posicao << '\n';
            this->num_elementos++;
            return;
        }

        if(i == 0)
            std::cout << "\tO elemento " << valor << " colide com "
                      << hash_table[posicao] << " na posicao " << posicao << '\n';

    }
    std::cout << "\t Elemento " << valor << " nao pode ser inserido.\n";

}

void hash_fechada::deletar(int valor)
{
    int TH_aux = this->TH, posicao;
    for(int i = 0; i < this->TH; i++)
    {
        if(this->tentativa == LINEAR)
        {
            posicao = (valor + i)% this->TH;
            if(i == 0)
            {
                std::cout << "Elemento para deletar " << valor << '\n';
                std::cout << "\t" << valor << " MOD " << this->TH << " = " << posicao << '\n';
            }
            else
                std::cout << "\t" << valor << '+' << i << " MOD " << this->TH << " = " << posicao << '\n';

        }
        else if(this->tentativa == QUADRATICA)
        {
            posicao = (valor + i*i)% this->TH;
            if(i == 0)
            {
                std::cout << "Elemento para deletar " << valor << '\n';
                std::cout << "\t" << valor << " MOD " << this->TH << " = " << posicao << '\n';
            }
            else
                std::cout << "\t" << valor << '+' << i << "^2 MOD " << this->TH << " = " << posicao << '\n';
        }
        else if(this->tentativa == DUPLO_HASHING)
        {
            posicao = valor % TH_aux;
            if(i == 0)
            {
                std::cout << "Elemento para deletar " << valor << '\n';
                std::cout << "\tTH(" << i << ")=" << TH_aux << ",\t" << valor <<
                             " MOD " << TH_aux << " = " << posicao << '\n' ;
            }
            else
                std::cout << "\tTH(" << i << ")=" << TH_aux << ",\t" << valor <<
                             " MOD " << TH_aux << " = " << posicao << '\n';

            TH_aux = prox_menor_primo(TH_aux);
        }

        if(hash_table[posicao] == valor)
        {
            hash_table[posicao] = -1;
            std::cout << "\tElemento " << valor << " removido no indice " << posicao << '\n';
            return;
        }

    }
    std::cout << "\t Elemento " << valor << " nao pode ser deletado na hash.\n";
}

int hash_fechada::prox_menor_primo(int numero)
{
    while(numero > 2)
    {
        numero--;
        bool check = true;
        for(int i = 2; i*i <= numero; ++i)
            if(numero%i == 0){
                check = false;
                break;
             }

        if(check)
            return numero;
    }

    return 2;
}

void hash_fechada::print()
{
    for(int i = 0; i < this->TH; i++)
    {
        std::cout << "Posicao " << i;
        if(hash_table[i] == -1)
            std::cout << " -> X\n";
        else
            std::cout << " -> [" << hash_table[i] << "]\n";
    }
}

double hash_fechada::balance_factor()
{
    int amount = 0;
    for(int i = 0; i < this->TH; i++)
        if(this->hash_table[i] != -1)
            amount++;

    return double(amount)/double(this->TH);
}
