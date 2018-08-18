#ifndef DTREE_HPP
#define DTREE_HPP

#include <string>
#include <bitset>
#include <vector>
#include <queue>
#include <iostream>
#include <utility>
#include <iomanip>
#include <cmath>

struct node
{
    std::string value;
    std::string answer;
    std::string ansl;
    std::string ansr;
    node *right, *left;
    node(const std::string &_value,
         const std::string &_answer) : value(_value),
                                  answer(_answer),
                                  right(nullptr),
                                  left(nullptr) {}
};

class DTree
{
public:
    node *root;
    int height;
public:
    DTree();
    virtual ~DTree();
    node* initialize();
    void insert(const std::string &_question);
    void remove(const std::string &_question);

    void create (const std::vector<std::string> &_list);
    node* search(const std::string &_chain);
    void prune(const std::string &_property);
    void show(node *_root, int indent);
};

#endif
