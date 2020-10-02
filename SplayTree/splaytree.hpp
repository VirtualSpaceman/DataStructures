#ifndef SPLAYTREE_HPP
#define SPLAYTREE_HPP
#include <vector>
#include <utility>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <iomanip>
#include "node.hpp"

class splaytree
{
public:
    splaytree();
    void insert(Node *&root, int element);
    void remove(Node *&root, int element);
    bool find(Node *&root, int element);
    void print(Node *&root, int n);
    Node *root;

private:
    void zag(Node *&root);
    void zig(Node *&root);
    void zagZig(Node *&root);
    void zagZag(Node *&root);
    void zigZag(Node *&root);
    void zigZig(Node *&root);
    int findPath(Node *&root, int element);
    void inOrder(Node *&root);
    Node *min(Node *&root);
    void splay(int element, Node *&root, bool flag);
    void randomSearches(int number);
    void printSearches(std::vector<int> &search);

};

#endif // SPLAYTREE_HPP
