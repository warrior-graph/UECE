from acao_invalida_exception import AcaoInvalidaException
from animal import Animal
from tipo_elemento import TipoElemento


class Rato(Animal):
    #Atributo que representa o peso de um objeto Rato
    __peso = 0
    #Atributo que representa o peso adicional de um objeto Rato
    __peso_adicional = 0

    def __init__(self, peso=0, peso_adicional=0, hp=0, nome="", tipo_elemento=None):
        super().__init__(nome, tipo_elemento, hp)
        self.__peso = peso
        self.__peso_adicional = peso_adicional

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @peso.deleter
    def peso(self):
        del self.__peso

    @property
    def peso_adicional(self):
        return self.__peso_adicional

    @peso_adicional.setter
    def peso_adicional(self, peso_adicional):
        self.__peso_adicional = peso_adicional

    @peso_adicional.deleter
    def peso_adicional(self):
        del self.__peso_adicional

    #Funcao que tenta carregar um pedaco de queijo tratadas as devidas excecoes
    def carregar(self, sala):
        try:
            if self.__peso_adicional > self.__peso:
                raise AcaoInvalidaException
            else:
                if sala.queijo.peso > 0 and sala.cenario[len(sala.cenario) - 1][len(sala.cenario) - 1] is self.tipo_elemento:
                    self.__peso_adicional += 20
                    sala.queijo.peso -= 20

                elif sala.queijo.peso == 0:
                    sala.cenario[len(sala.cenario) - 1][len(sala.cenario) - 1] = TipoElemento.Espaco_Vazio.value
        except AcaoInvalidaException as excesso:
            excesso.excesso_de_peso()
    #Funcao que descarrega o queijo sempre que o objeto Rato estiver na posicao 0, 0
    def descarregar(self, sala):
        if sala.cenario[0][0] is self.tipo_elemento:
            self.__peso_adicional = 0
        else:
            return
    #Funcao que retorna True ou False se o objeto Rato esta na posicao do queijo
    def tenho_queijo(self, sala):
        if sala.cenario[len(sala.cenario) - 1][len(sala.cenario) - 1] is self.tipo_elemento:
            return True
        else:
            return False



