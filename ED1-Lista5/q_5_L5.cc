#include <bits/stdc++.h>

using namespace std;

struct cliente
{
    string nome, cpf;
    cliente *next, *prev;
    cliente(string _nome, string _cpf){nome = _nome, cpf = _cpf, next = nullptr, prev = nullptr;}
    cliente(){next = nullptr, prev = nullptr;}
};

cliente* criar()
{
    cliente *head = new cliente();
    return head;
}

void inserir(cliente *head, string nome, string cpf, int pos)
{
    cliente *aux = head, *c = new cliente(nome, cpf);
    int i = 1;
    while(i < pos and aux->next != nullptr)
        aux = aux->next, i++;

    if(aux->next == nullptr)
        aux->next = c, c->prev = aux, c->next = nullptr;
    else
        c->next = aux->next, c->next->prev = c, aux->next = c, c->prev = aux;
}

cliente remover(cliente *head, int pos)
{
    cliente *aux = head->next, r;
    int i = 1;
    while(i < pos and aux->next != nullptr)
        aux = aux->next, i++;
    r = *aux;
    if(aux->next == nullptr)
        aux->prev->next = nullptr;
    else
        aux->prev->next = aux->next, aux->next->prev = aux->prev;
    return r;
}

int buscar(cliente *head, cliente *c)
{
    cliente *aux = head->next;
    int i = 1;
    while(aux->cpf != c->cpf)
        aux = aux->next, i++;
    return i;
}


void listar(cliente *head)
{
    cliente *aux = head->next;
    while(aux != nullptr)
        cout << aux->nome << '\n', aux = aux->next;
}

void deletar(cliente *head)
{
	cliente *aux = head;
    while(aux->next != nullptr)
        aux = aux->next, delete(head), head = aux->next;
}

int main()
{
	cliente *head = criar();
	inserir(head, "batore", "123", 1);
	inserir(head, "ladesc", "242424", 1);
	cout << remover(head, 1).nome << '\n';
	cout << remover(head, 1).nome << '\n';
	deletar(head);
	
    return 0;
}
