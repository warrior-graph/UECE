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

void inserir(cliente *head, string nome, string cpf)
{
    cliente *aux = head, *c = new cliente(nome, cpf);;
    while(aux->next != nullptr)
        aux = aux->next;
    aux->next = c;
}

cliente remover(cliente *head)
{
    cliente *aux = head->next, r = *aux;
    if(aux->next == nullptr)
        head->next = nullptr;
    else
        head->next = aux->next;
    delete(aux);
    return r;
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
    inserir(head, "mendes", "11");
    inserir(head, "jaspion", "22");
    cout << remover(head).nome << '\n';
    cout << remover(head).nome << '\n';
    deletar(head);

    return 0;
}
