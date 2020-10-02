#ifndef NODE_HPP
#define NODE_HPP


class Node
{
public:
    Node(int element, int height = 0);
    int element;
    int height;
    Node *left;
    Node *right;
};

#endif // NODE_HPP
