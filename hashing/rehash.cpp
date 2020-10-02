#include "rehash.hpp"

reHash::reHash(int TH)
{
    //funcao para iniciar o tamanho de TH e colocar -1 para simbolizar celulas vazias
    this->TH = TH;
    hash.resize(this->TH);
    std::fill(hash.begin(), hash.end(), -1);
    this->num_elementos = 0;

}

//funcao para inserir na tabela hash
void reHash::inserir(int valor)
{
    //Se na hora da inserir a hash estiver com TH/2 +1 elementos, fazer rehashing
    if(this->full() > HASH_CHEIA)
    {
        std::cout << "A hash cheia. O rehashing e necessario\n";
        this->rehashing();
    }

    for(int i = 0; i < this->TH; i++)
    {
        //Tentativa quadratica de insercao
        int indice = (valor + i*i)%this->TH;
        std::cout << "Elemento: " << valor;
        std::cout << "\t" << valor << " + " << i << "^2 MOD "<< this->TH<< " = " << indice << '\n';

        //Se o hash[posicao] estiver vazio, ou seja, com -1, poderei inserir
        if(hash[indice] == -1)
        {
            //insere elemento na posicao [indice] e incrementa a quantidade de elementos na hash
            hash[indice] = valor;
            this->num_elementos += 1;
            std::cout << "\tElemento " << valor << " inserido no indice " << indice << '\n';
            return;
        }
        if (i == 0)
            std::cout << "\t Colidiu com " << hash[indice] << " na posicao " << indice << '\n';
    }
    std::cout << "O elemento " << valor << " nao pode ser inserido. O rehashing e necessario para"
                                           "a insersao do elemento\n";
    //Se nao conseguir inserir o elemento, fazer rehashing e inserir o elemento
    this->rehashing();
    this->inserir(valor);
}

void reHash::deletar(int valor)
{
    //se a hash nao estiver vazia
    if(!this->empty())
    {
        //usar tentativa quadratica para a remocao
        for(int i = 0; i < this->TH; i++)
        {
            int indice = (valor + i*i)% this->TH;

            if(i == 0)
            {
                std::cout << "Elemento para deletar " << valor << '\n';
                std::cout << "\t" << valor << " MOD " << this->TH << " = " << indice << '\n';
            }
            else
                std::cout << "\t" << valor << '+' << i << "^2 MOD " << this->TH << " = " << indice << '\n';

            //se a a hash nao estiver vazia na posicao hash[indice] e hash[indice] for igual ao elemento procurado
            if(hash[indice] != -1 and hash[indice] == valor)
            {
                //remove o elemento colocando -1 na posicao
                hash[indice] = -1;
                //decrementa o contador de elementos na hash
                this->num_elementos--;
                std::cout << "\tElemento " << valor << " deletado no indice " << indice << '\n';
                return;
            }
        }
        std::cout << "\t Elemento " << valor << " nao esta na hash.\n";
    }
}

//funcao para verificar se a hash esta vazia
bool reHash::empty()
{
    for(int i = 0; i < this->TH; ++i)
        if(hash[i] != -1)
            return false;

    return true;
}

//funcao para retornar se a hash esta metade cheia
double reHash::full()
{
    return (double)(this->num_elementos)/(double)this->TH;
}

//funcao para encontrar o primo mais proximo
int reHash::primo_mais_prox(int numero)
{
    while(true)
    {
        numero++;
        bool check = true;
        for(int i = 2; i*i <= numero; ++i)
            if(numero%i == 0){
                check = false;
                break;
             }

        if(check)
            return numero;
    }
}

//funcao que realiza o rehashing
void reHash::rehashing()
{
    this->num_elementos = 0;
    //cria uma tabela hash auxiliar
    std::vector<int> hash_table_aux = std::vector<int>(this->TH);
    //salva o TH antigo
    int th_antigo = this->TH;

    //salva a tabela atual na auxiliar
    for(int i = 0; i < this->TH; i++)
        hash_table_aux[i] = hash[i];

    //Encontra o primo mais proximo do dobro do tamanho atual
    this->TH = primo_mais_prox(2*this->TH);
    //Expande a tabela para o dobro do primo atual
    this->hash = std::vector<int>(this->TH);
    std::fill(this->hash.begin(), this->hash.end(), -1);
    std::cout << "O novo tamanho da hash e: " << this->TH << ". Agora vamos inserir os valores para a nova hash.\n";

    //Insere na nova tabela hash os elementos antigos
    for(int i= 0; i < th_antigo; i++)
        if(hash_table_aux[i] != -1)
            this->inserir(hash_table_aux[i]);
}

//funcao para mostrar o estado atual da tabela hash
void reHash::print()
{
    for(int i = 0; i < this->TH; i++)
    {
        std::cout << "\nPosicao " << i;
        if(hash[i] == -1)
            std::cout << " -> X";
        else
            std::cout << " -> [" << hash[i] << "]";
    }
    std::cout << '\n';
}