#include "node.hpp"
#include "splaytree.hpp"

splaytree::splaytree()
{

}

Node* splaytree::min(Node *&root)
{
    if(root == nullptr)
        return nullptr;
    if(root->left == nullptr)
        return root;
    return min(root->left);
}

void splaytree::splay(int element, Node *&root, bool flag)
{
    if(root == nullptr or root->element == element)
        return;

    if(flag)
    {
        if(element < root->element)
        {
            splay(element, root->left, false);
            if(element == root->left->element)
                zig(root);
        }
        else if(element > root->element)
        {
            splay(element, root->right, false);
            if(element == root->right->element)
                zag(root);
        }
    }
    if(element < root->element)
    {
        if(root->left == nullptr)
            return;

        else if(element < root->left->element)
        {
            splay(element, root->left->left, false);
            if(root->left->left != nullptr and element == root->left->left->element)
                zigZig(root);
        }
        else if(element > root->left->element)
        {
            splay(element, root->left->right, false);
            if(root->left->right != nullptr and element == root->left->right->element)
                zagZig(root);
        }
        else if(root->left != nullptr)
        {
            if(root->left->element == element)
                zig(root);
        }
    }
    else
    {
        if(root->right == nullptr)
            return;

        else if(element < root->right->element)
        {
            splay(element, root->right->left, false);
            if(root->right->left != nullptr and element == root->right->left->element)
                zigZag(root);
        }
        else if(element > root->right->element)
        {
            splay(element, root->right->right, false);
            if(root->right->right != nullptr and element == root->right->right->element)
                zagZag(root);
        }
        else if(root->right != nullptr)
        {
            if(root->right->element == element)
                zag(root);
        }
    }

}

void splaytree::zag(Node *&root)
{
    Node* aux;

    aux = root->right;
    root->right = aux->left;
    aux->left = root;
    root = aux;
}

void splaytree::zig(Node *&root)
{
    Node* aux;

    aux = root->left;
    root->left = aux->right;
    aux->right = root;
    root = aux;
}

void splaytree::zagZig(Node *&root)
{
    Node* aux1 = root->left;
    Node* aux2 = aux1->right;

    aux1->right = aux2->left;
    aux2->left = aux1;
    root->left = aux2->right;
    aux2->right = root;
    root = aux2;
}

void splaytree::zigZag(Node *&root)
{
    Node* aux1 = root->right;
    Node* aux2 = aux1->left;

    aux1->left = aux2->right;
    aux2->right = aux1;
    root->right = aux2->left;
    aux2->left = root;
    root = aux2;
}

void splaytree::zigZig(Node *&root)
{
    Node* aux1 = root->left;
    root->left = aux1->right;
    aux1->right = root;
    root = aux1;

    Node* aux2 = root->left;
    root->left = aux2->right;
    aux2->right = root;
    root = aux2;
}

void splaytree::zagZag(Node *&root)
{
    Node* aux1 = root->right;
    root->right = aux1->left;
    aux1->left = root;
    root = aux1;

    Node* aux2 = root->right;
    root->right = aux2->left;
    aux2->left = root;
    root = aux2;
}

void splaytree::insert(Node *&root, int element)
{
    if(root == nullptr)
        root = new Node(element);
    else if(element < root->element)
        insert(root->left, element);
    else if(element > root->element)
        insert(root->right, element);
}

void splaytree::remove(Node *&root, int element)
{
    if(root == nullptr)
        return;
    if(element < root->element)
        remove(root->left, element);
    else if(element > root->element)
        remove(root->right, element);
    else if(root->left != nullptr and root->right != nullptr)
    {
        root->element = min(root->right)->element;
        remove(root->right, element);
    }
    else
    {
        Node* aux = root;
        if(root->left != nullptr)
            root = root->left;
        else
            root = root->right;

        delete aux;
    }
}

int splaytree::findPath(Node *&root, int element)
{
    if(root == nullptr)
        return 0;

    int pathLenght = 1;
    if(element < root->element)
        pathLenght += findPath(root->left, element);
    else if(element > root->element)
        pathLenght += findPath(root->right, element);

    return pathLenght;
}

bool splaytree::find(Node *&root, int element)
{
    int length = findPath(root, element);

    if(length%2)
    {
        splay(element, root, false);
        if(element == root->element)
            return true;
        else
            return false;
    }
    else
    {
        splay(element, root, true);
        if(element == root->element)
            return true;
        else
            return false;
    }
}

void splaytree::randomSearches(int number)
{
    std::vector<std::pair<int, int>> searches;
    int element, frequency;
    for(int i = 0; i < number; i++)
    {
        std::cout << "Elemento " << i+1<< " frequencia" << i+1 << '\n';
        std::cin >> element >> frequency;
        searches.push_back(std::make_pair(element, frequency));
    }

    std::srand(std::time(nullptr));

    std::vector<int> sequences;
    while(number)
    {
        int position = std::rand() % searches.size();
        if(searches[position].second > 0)
        {
            sequences.push_back(searches[position].first);
            bool aux = find(this->root, searches[position].first);
            searches[position].second--;
            if(searches[position].second == 0)
                number--;

        }
    }
}

void splaytree::print(Node *&root, int n)
{
    if(root != nullptr)
    {
        if(root->right)
        {
            print(root->right, n+4);
        }
        if(n)
        {
            std::cout << std::setw(n) << ' ';
        }
        if(root->right)
        {
            std::cout<<" /\n" << std::setw(n) << ' ';
        }
        std::cout << root->element << "\n";
        if(root->left)
        {
            std::cout << std::setw(n) << ' ' << " \\\n";
            print(root->left, n+4);
        }
    }
}
