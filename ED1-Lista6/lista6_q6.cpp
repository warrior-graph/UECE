#include <iostream>
#include <string>

using namespace std;

struct Node
{
    std::string name;
    Node *next;
    Node(Node *_next, std::string _name) : name(_name),
																					 next(_next){}
    Node(): next(nullptr) {}
};

Node* create()
{
    Node *head = new Node();
    head->next = head;
    return head;
}

void insert_node(Node *head, string name, int pos)
{
    Node *aux;
    int i = 0;
    for(aux = head; aux->next != head and i < pos; aux = aux->next)
        i++;
    if(aux->next == head)
        aux->next = new Node(head, name);
    else
    {
        Node *k = new Node(head, name);
        k->next = aux->next;
        aux->next = k;
    }
}

Node remove(Node *head, int pos)
{
    Node *aux;
    int i = 0;
    for(aux = head; aux->next != head and i < pos; aux = aux->next)
        i++;
    Node *k = aux->next, r = *k;
    aux->next = aux->next->next;
    delete(k);
    return r;
}

void clean(Node *head){
    Node *aux1 = head->next, *aux2 = head->next;
    while(aux1 != head)
        aux1 = aux1->next, delete(aux2), aux2 = aux1;
    delete(aux2);
}

std::string solve(Node *head, int n, int m)
{
    int c = 0, i;
    Node *aux = head;
    while(n != 1)
    {
        if(aux == head)
            i = -1, aux = aux->next;
        else
        {
            i++, c++;
            if(c == m)
            {
                Node r = remove(head, i);
                n--, i--, c = 0;
                aux = r.next;
            }
						else
                aux = aux->next;
        }
    }
    return head->next->name;
}

int main()
{
    Node *head = create();
    insert_node(head, "Chengas", 0);
    insert_node(head, "Chingas", 1);
    insert_node(head, "Chongas", 2);
    insert_node(head, "Chungas", 3);
    insert_node(head, "Changas", 4);
    cout << solve(head, 5, 2) << '\n';
    clean(head);
    return 0;
}
