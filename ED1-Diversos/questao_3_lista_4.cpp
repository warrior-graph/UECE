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

void inserir(cliente *lista, const string &nome, const string &cpf)
{

    lista[tam] = cliente(nome, cpf);
    tam++;
}

cliente remover(cliente *lista)
{
    tam--;
    return lista[tam];
}

void deletar(cliente *lista)
{
    lista = nullptr;
}

int main()
{

    cliente *lista = criar();

    inserir(lista, "pedro", "123321");
    inserir(lista, "monteiro", "321321");
    cout << remover(lista).nome << "\n" << remover(lista).nome << '\n';
    deletar(lista);
    return 0;
}
