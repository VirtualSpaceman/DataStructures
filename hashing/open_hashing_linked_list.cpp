#include "open_hashing_linked_list.hpp"

template<class T>
open_hashing_linked_list<T>::open_hashing_linked_list(int TH)
{
    this->TH = TH;
    this->hash.resize(TH);
}

template<class T>
void open_hashing_linked_list<T>::insert_element(T data)
{
    //calcula a posicao para inserir o elemento
    int position = data%this->TH;
    std::cout << "Elemento para inserir " << data << '\n';
    std::cout << "\t" << data << " MOD " << this->TH << " = " << position << '\n';
    //insere o elemento na lista da posicao calculada
    hash[position].push_front(data);
}

template<class T>
void open_hashing_linked_list<T>::remove_element(T data)
{
    //calcula a posicao para remover
    int position = data%this->TH;

    //se a posicao nao tiver vazia
    if(!hash[position].empty())
    {
        //realiza a busca na lista
        for(T &element: hash[position])
            //se encontrar o elemento, a remocao e realizada
            if(element == data){
                hash[position].remove(data);
                return;
            }
        std::cout << "Elemento nao encontrado\n";
    }

    else
        std::cout << "Elemento nao encontrado\n";
}

template<class T>
int open_hashing_linked_list<T>::search_element(T data)
{
    //procura o elemento dentro das listas da TH
    for(int i = 0; i < (int)hash.size(); ++i)
    {
        if(!hash[i].empty())
        {
            for(T &element: hash[i])
                //se encontrar o elemento, retorna a posicao em que foi encontrado
                if(element == data)
                    return i;
        }
    }
    //caso contrario, retorna -1
    return -1;
}

//funcao para mostrar o estado atual da hash
template<class T>
void open_hashing_linked_list<T>::show_hash()
{
    for(int i = 0; i < TH; ++i)
    {
        std::cout << "Posicao " << i << ": ";
        if(!hash[i].empty())
            for(T &elem: hash[i])
                std::cout << elem <<" -> ";
        std::cout << "x \n";
    }
}

template<class T>
double open_hashing_linked_list<T>::FB()
{
    int qtde = 0, fator_de_carga = 0;
    for(int i = 0; i < this->TH; i++)
    {
        fator_de_carga = std::max(fator_de_carga, (int)hash[i].size());
        qtde += (int)hash[i].size();
    }
    std::cout << "O fator de balanceamento e: " << double(qtde)/double(this->TH*fator_de_carga) << '\n';
    std::cout << "O fator de carga e: " << fator_de_carga << '\n';
}

template class open_hashing_linked_list<int>;