from random import randint
from tipo_elemento import TipoElemento
from rato import Rato
from gato import Gato


class Sala():
    #Atributo que representa um cenario do objeto Sala
    __cenario = []
    #Atributo que representa um objeto Rato padrao para facilitar a inicializacao do cenario
    __rato_default = Rato(0, 0, 0, "", TipoElemento.Rato.value)
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
    def quejo(self):
        del self.__queijo_default

    #Inicializa um cenario preenchido com elementos Espaco_Vazio e posicoes todos os personagens e objetos
    #do cenario
    def inicializar(self, n):

        for i in range(n):
            self.__cenario.append([])
        for i in self.__cenario:
            for j in range(n):
                i.append(TipoElemento.Espaco_Vazio.value)

        posicoes = int(n / 2)

        k = 0
        tup_list = []
        #gera uma posicao randomica e faz uma lista de tuplas com coordenadas randomicas
        while k <= posicoes:
            l = randint(1, n - 2)
            m = randint(1, n - 2)
            tup = l, m
            if tup not in tup_list:
                tup_list.append(tup)
                k += 1
        #Sem perda de generalidade, defino a ultima posicao da lista de tuplas como sendo a tupla de posicao do objeto
        #gato
        posicao_gato = tup_list[posicoes]
        del tup_list[posicoes]
        #monto o cenario
        for i in tup_list:
            self.__cenario[i[0]][i[1]] = TipoElemento.Obstaculo.value
        self.__cenario[0][0] = self.__rato_default.tipo_elemento
        self.__cenario[posicao_gato[0]][posicao_gato[1]] = self.__gato_default.tipo_elemento
        self.__cenario[n - 1][n - 1] = self.__queijo_default
        o = 0
        #verifico se o numero de ebstaculos do cenario esta correto
        for i in self.__cenario:
            for j in i:
                if j is TipoElemento.Obstaculo.value:
                    o += 1

        if o < posicoes:
            self.inicializar(n)
        else:
            return
    #Esse metodo apaga os elementos Espaco_Vazio, da direita para a esquerda, ate encontrar qualquer objeto que nao seja
    #um Espaco_Vazio
    def vizualizar_cenario(self):

        matrix_dinamica = [i for i in self.__cenario]
        print(
            "\n#=====================================================================================================#")
        for i in matrix_dinamica:
            count = 0
            for j in i[::-1]:
                if j is TipoElemento.Espaco_Vazio.value:
                    i.pop()
                    count += 1
                else:
                    break
            print("  ", '\t'.join(i))
            for k in range(0, count):
                i.append(TipoElemento.Espaco_Vazio.value)
        print("#=====================================================================================================#")
