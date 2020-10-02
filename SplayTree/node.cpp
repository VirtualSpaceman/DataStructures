#include "node.hpp"

Node::Node(int element, int height)
{
    this->element = element;
    this->height = height;
    right = nullptr;
    left = nullptr;
}
