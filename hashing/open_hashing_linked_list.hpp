#ifndef OPENHASHINGLINKEDLIST_H
#define OPENHASHINGLINKEDLIST_H

#include <list>
#include <vector>
#include <iostream>

template <class T>
class open_hashing_linked_list
{
public:
    open_hashing_linked_list<T>(int TH);
    void insert_element(T data);
    void remove_element(T data);
    int search_element(T data);
    void show_hash();

private:

    int TH;
    std::vector<std::list<T>> hash;

};

#endif // OPENHASHINGLINKEDLIST_H
