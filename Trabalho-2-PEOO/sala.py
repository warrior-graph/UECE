from tipo_elemento import TipoElemento
from rato import Rato
from gato import Gato
from obstaculo import Obstaculo
from eresistencia import Eresistencia


class Sala():
    #Atributo que representa um cenario do objeto Sala
    __cenario = []
    #Atributo que representa um objeto Rato padrao para facilitar a inicializacao do cenario
    __rato_default = Rato(0, 0, 0, "", TipoElemento.Rato.value, "rato")
    # Atributo que representa um objeto Gato padrao para facilitar a inicializacao do cenario
    __gato_default = Gato("", TipoElemento.Gato.value, 0, "")
    # Atributo que representa um objeto Queijo padrao para facilitar a inicializacao do cenario
    __queijo_default = TipoElemento.Queijo.value

    def __init__(self, cenario=None):
        if cenario is None:
            cenario = []
        self.__cenario = cenario

    @property
    def cenario(self):
        return self.__cenario

    @cenario.setter
    def cenario(self, cenario):
        self.__cenario = cenario

    @cenario.deleter
    def cenario(self):
        del self.__cenario

    @property
    def rato(self):
        return self.__rato_default

    @rato.setter
    def rato(self, rato):
        self.__rato_default = rato

    @rato.deleter
    def rato(self):
        del self.__rato_default

    @property
    def gato(self):
        return self.__gato_default

    @gato.setter
    def gato(self, gato):
        self.__gato_default = gato

    @gato.deleter
    def gato(self):
        del self.__gato_default

    @property
    def queijo(self):
        return self.__queijo_default

    @queijo.setter
    def queijo(self, queijo):
        self.__queijo_default = queijo

    @queijo.deleter
    def queijo(self):
        del self.__queijo_default

    #Inicializa um cenario preenchido com elementos Espaco_Vazio e posicoes todos os personagens e objetos
    #do cenario
    def inicializar(self, arquivo):
        #aqui o arquivo e' lido e todas as instrucoes sao executadas na criacao de um cenario
        with open(arquivo, "r") as file:
            lista_de_instrucoes = file.readlines()

        n = int(lista_de_instrucoes[0])

        numero_obstaculos = int(lista_de_instrucoes[2])

        for i in range(n):
            self.__cenario.append([])
        for i in self.__cenario:
            for j in range(int(lista_de_instrucoes[0])):
                i.append(TipoElemento.Espaco_Vazio.value)

        self.__cenario[int(lista_de_instrucoes[1][0])][int(lista_de_instrucoes[1][2])] = self.gato.tipo_elemento

        for i in range(0, numero_obstaculos):
            if lista_de_instrucoes[i+3][4] is 'R':
                self.__cenario[int(lista_de_instrucoes[i + 3][0])][int(lista_de_instrucoes[i + 3][2])] = Obstaculo("multilaser", Eresistencia.resistente)
            else:
                self.__cenario[int(lista_de_instrucoes[i + 3][0])][int(lista_de_instrucoes[i + 3][2])] = Obstaculo("ibyte", Eresistencia.fragil)

        self.__cenario[0][0] = self.rato.tipo_elemento
        self.__cenario[n - 1][n - 1] = self.queijo

    #Esse metodo apaga os elementos Espaco_Vazio, da direita para a esquerda, ate encontrar qualquer objeto que nao seja
    #um Espaco_Vazio
    def vizualizar_cenario(self):

        matrix_dinamica = [i for i in self.__cenario]
        print("\n#=====================================================================================================#")
        for i in matrix_dinamica:
            count = 0
            for j in i[::-1]:
                if j is TipoElemento.Espaco_Vazio.value:
                    i.pop()
                    count += 1
                else:
                    break
            print(i)
            for k in range(0, count):
                i.append(TipoElemento.Espaco_Vazio.value)
        print("#=====================================================================================================#")
