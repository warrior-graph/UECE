#include "dtree.hpp"

DTree::DTree()
{
    root = nullptr;
    height = -1;
}

void DTree::insert(const std::string &_question)
{
    height++;
    int ans = pow(2, height - 1) - 1, al, ar;
    std::queue<node*> q;
    if(root == nullptr)
    {
        root = new node(_question, std::bitset<8>(height).to_string());
        return;
    }
    node* aux;
    q.push(root);
    while(!q.empty())
    {
        aux = q.front(), q.pop();
        if(aux->left != nullptr)
            q.push(aux->left), q.push(aux->right);
        else
        {
            al = 2* ans + 1, ar = 2 * ans;
            aux->left = new node(_question, "-->" + std::bitset<8>(al).to_string()),
            aux->right = new node(_question, "-->" + std::bitset<8>(ar).to_string());
            ans--;
        }
    }

}

void DTree::remove(const std::string &_question)
{
    std::vector<std::string> aux_l;
    if(root == nullptr)
        { std::cout << "Property does not exist\n";  return;}
    std::queue<node*> q;
    node* aux;
    q.push(root);
    while(!q.empty())
    {
        aux = q.front(), q.pop();
        if(aux->value != _question)
            aux_l.push_back(aux->value);
        if(aux->left != nullptr)
            q.push(aux->left);
    }
    q.push(root);
    while(!q.empty())
    {
        aux = q.front(), q.pop();
        if(aux->left != nullptr)
            q.push(aux->left), q.push(aux->right);
        delete(aux);
    }
    root = nullptr;
    create(aux_l);
    height--;
}

void DTree::create(const std::vector<std::string> & _list)
{
    height = -1;
    std::queue<node*> q;
    node* aux;
    if(root == nullptr)
        for(const std::string &i : _list) insert(i);
    else
    {
        q.push(root);
        while(!q.empty())
        {
            aux = q.front(), q.pop();
            if(aux->left != nullptr)
                q.push(aux->left), q.push(aux->right);
            delete(aux);
        }
        root = nullptr;
        create(_list);
    }

    int ans = pow(2, height) - 1;
    q.push(root);
    while(!q.empty())
    {
        aux = q.front(), q.pop();
        if(aux->left != nullptr)
            q.push(aux->left), q.push(aux->right);
        else
        {
            int al = 2* ans + 1, ar = 2 * ans;
            aux->left = new node("leaf", "-->" + std::bitset<8>(al).to_string()),
            aux->right = new node("leaf", "-->" + std::bitset<8>(ar).to_string());
            ans--;
        }
    }
}

node* DTree::search(const std::string &_chain)
{
    if(root == nullptr)
        return nullptr;
    node* it = root;
    for(const char &i : _chain)
        if(i == '0')
            if(it->right == nullptr)
                return nullptr;
            else it = it->right;
        else
            if(it->left == nullptr)
                return nullptr;
            else it = it->left;
    return it;
}

void DTree::show(node *_root, int indent)
{
    if(_root != nullptr)
    {
        if(_root->right)
            show(_root->right, indent + 5);
        if (indent)
            std::cout << std::setw(indent) << ' ';
        if (_root->right) std::cout<<" /\n" << std::setw(indent) << ' ';
        std::cout<< '(' << _root->value << ')'
                 << (_root->left == nullptr ? _root->answer : "") << "\n";
        if(_root->left)
        {
            std::cout << std::setw(indent) << ' ' <<" \\\n";
            show(_root->left, indent + 5);
        }
    }
}

void DTree::prune(const std::string &property)
{
    std::queue<node*> q, q1;
    node *aux, *aux2;
    q.push(root);
    while(!q.empty())
    {
        aux = q.front(), q.pop();
        if(aux->value == property)
            if(aux->left != nullptr)
            {
                q1.push(aux->left);
                while(!q1.empty())
                {
                    aux2 = q1.front(), q1.pop();
                    aux2->answer = "-X-cut";
                    if(aux2->left != nullptr)
                        q1.push(aux2->left), q1.push(aux2->right);
                }
            }
            else aux->answer = "-X-cut";
        if(aux->left != nullptr)
            q.push(aux->left), q.push(aux->right);
    }
}

DTree::~DTree()
{}
