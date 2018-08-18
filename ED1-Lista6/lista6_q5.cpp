#include <iostream>

using namespace std;

struct Node
{
    int value;
    Node *next;
    Node(int _value) : value(_value), next(nullptr) {}
    Node() : next(nullptr) {}
};

struct begin_node
{
    Node *adj, *end;
    bool flag;
};

begin_node* create(int n)
{
    begin_node *head = new begin_node[n];
    for(int i = 0; i < n; i++)
        head[i].adj = new Node(), head[i].flag = false, head[i].end = head[i].adj;
    return head;
}

void insert_node(begin_node *head, int v, int w)
{
    head[v].end->next = new Node(w);
    head[v].end = head[v].end->next;
    head[v].adj->value++;
    return;
}

void dfs(begin_node *head, int v)
{
    head[v].flag = true;
    for(Node *aux = head[v].adj->next; aux != nullptr; aux = aux->next)
        if(!head[aux->value].flag)
            dfs(head, aux->value);
}

void clean(begin_node *head, int n)
{
    Node *aux, *k;
    for(int i = 0; i < n; i++){
        aux = head[i].adj;
        while(aux != nullptr)
            k = aux->next, delete(aux), aux = k;
    }
    delete[] head;
}

void show(begin_node *head, int n)
{
    for(int i = 0; i < n; i++)
    {
        cout << i << ": ";
        for(Node *aux = head[i].adj->next; aux != nullptr; aux = aux->next)
            cout << aux->value << ' ';
        cout << '\n';
    }
}

int main()
{
    begin_node *head = create(3);
    insert_node(head, 0, 2);
    insert_node(head, 2, 0);
    insert_node(head, 0, 1);
    insert_node(head, 1, 0);
    insert_node(head, 1, 2);
    insert_node(head, 2, 1);
    show(head, 3);
    int ans = 0;
    for(int i = 0; i < 3; i++)
        if(!head[i].flag) dfs(head, i), ans++;
    cout << ans << '\n';
    clean(head, 3);
    return 0;
}
