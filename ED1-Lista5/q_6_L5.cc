#include <bits/stdc++.h>

using namespace std;

struct cliente
{
    string nome, cpf;
    cliente *next;
    cliente(string _nome, string _cpf, cliente *head){nome = _nome, cpf = _cpf, next = head;}
    cliente(){}
};

cliente* criar()
{
    cliente *head = new cliente();
    head->next = head;
    return head;
}

void inserir(cliente *head, string nome, string cpf, int pos)
{
    cliente *aux = head, *c = new cliente(nome, cpf, head);
    int i = 1;
    while(i < pos and aux->next != head)
        aux = aux->next, i++;
    if(aux->next == head)
        aux->next = c;
    else
        c->next = aux->next, aux->next = c;
}

cliente remover(cliente *head, int pos)
{
    cliente *aux = head, r, *k;
    int i = 1;
    while(i < pos)
        aux = aux->next, i++;
    r = *(aux->next);
    if(aux->next->next == head)
        delete(aux->next), aux->next = head;
    else
        k = aux->next, aux->next = aux->next->next, delete(k);
    return r;
}

int buscar(cliente *head, string cpf)
{
    cliente *aux = head->next;
    int i = 1;
    while(aux->cpf != cpf)
    {
        aux = aux->next, i++;
        if(aux == head)
            return -1;
    }
    return i;
}

void listar(cliente *head)
{
    cliente *aux = head->next;
    while(aux != head)
        cout << aux->nome << '\n', aux = aux->next;
}

void deletar(cliente *head)
{	
	cliente *aux = head, *r = head;
    while(aux->next != r)
        aux = aux->next, delete(head), head = aux->next;
}

int main()
{
	cliente *head = criar();
	inserir(head, "celestino", "321", 1);
	inserir(head, "jorge", "123", 1);
	listar(head);
	cout << buscar(head, "123") << '\n';
	cout << remover(head, 1).nome << '\n';
	cout << remover(head, 1).nome << '\n';
	deletar(head);
	
    return 0;
}
