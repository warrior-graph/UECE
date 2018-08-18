#include <iostream>
#include <string>

using namespace std;

int tam;

struct cliente
{
    string nome, cpf;
    cliente(const string &_nome, const string &_cpf) :
                                                      nome(_nome),
                                                      cpf(_cpf)
                                                      {}
    cliente() : nome(""), cpf("") {}

};

cliente* criar(const int MAX = 1 << 17)
{
    cliente* aux = new cliente [MAX];
    return aux;
}

void inserir(cliente* lista, const string &nome, const string &cpf, int pos)
{
    cliente aux, newcli(nome, cpf);
    for(; pos != tam; pos++)
        aux = lista[pos], lista[pos] = newcli, newcli = aux;
    lista[pos] = newcli;
    tam++;
}

cliente remover(cliente *lista, int pos)
{
    cliente aux = lista[pos];
    for(int i = pos; i < tam; i++);
        lista[pos] = lista[pos + 1];
    tam--;
    return aux;
}

int buscar(cliente *lista, const string &cpf)
{
    for(int i = 0; i < tam; i++)
        if(lista[i].cpf == cpf)
            return i;
    return -1;
}

void deletar(cliente *lista)
{
    lista = nullptr;
}

int main()
{
    cliente *lista = criar();
    inserir(lista, "monteiro galdino", "123321", 0);
    cout << lista[0].nome << '\n';
    cliente r = remover(lista, 0);
    cout << lista[0].nome << '\n';
    deletar(lista);
    return 0;
}
