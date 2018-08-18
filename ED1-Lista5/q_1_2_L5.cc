#include <bits/stdc++.h>

using namespace std;

struct cliente
{
    string nome, cpf;
    cliente *next;
    cliente(string _nome, string _cpf){nome = _nome, cpf = _cpf, next = nullptr;}
    cliente(){next = nullptr;}
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
        aux->next = c;
    else
        c->next = aux->next, aux->next = c;
}

cliente remover(cliente *head, int pos)
{
    cliente *aux = head, r, *k;
    int i = 1;	
    while(i < pos and aux->next)
        aux = aux->next, i++;
    r = *(aux->next);
    if(aux->next->next == nullptr)
        aux->next = nullptr, delete(aux->next);
    else
    	k = aux->next->next, delete(aux->next), aux->next = k;
    return r;
}

int buscar(cliente *head, string cpf)
{
    cliente *aux = head->next;
    int i = 1;
    while(aux->cpf != cpf)
        aux = aux->next, i++;
    return i;
}


void listar(cliente *head)
{
    cliente *aux = head->next;
    while(aux != nullptr)
        cout << aux->nome << ' ' << aux->cpf << '\n', aux = aux->next;
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
	inserir(head, "galdino", "220", 1);
	inserir(head, "monteiro", "0101", 1);
	listar(head);
	cout << buscar(head, "220") << '\n';
	cout << remover(head, 1).nome << '\n';
	listar(head);
	deletar(head);

    return 0;
}
