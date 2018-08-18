#Essa classe tem por finalidade imprimir os erros gerados pelo metodo mover() da classe Animal

class AcaoInvalidaException(Exception):

    # Imprime um erro na tela e recebe uma string com uma informacao, por exemplo: o nome do animal.
    def extrapolar(self, warning):
        print("Cuidado, " + warning + ", para nao cair no abismo!!!")

    # Imprime um erro na tela e recebe uma string com uma informacao, por exemplo: o nome do animal.
    def obstaculo(self, warning):
        print("Impossivel passar por aqui, " + warning + ", a passagem parece estar bloqueada")

    # Imprime um erro na tela e recebe uma string com uma informacao, por exemplo: o nome do animal.
    def fuga_do_rato(self, warning):
        print("Por pouco voce nao foi pego pelo gato, " + warning)

    # Imprime um erro na tela
    def excesso_de_peso(self):
        print("Ta pesado!")

