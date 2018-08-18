from animal import Animal


class Gato(Animal):
    __estado = ""
    __contador_rodada = 0
    def __init__(self, nome="", tipo_elemento= None, hp=0, estado="", contador_rodada = 0):
        super().__init__(nome, tipo_elemento, hp)
        self.__estado = estado
        self.__contador_rodada = contador_rodada

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    @estado.deleter
    def estado(self):
        del self.__estado

    @property
    def contador_rodada(self):
        return self.__contador_rodada

    @contador_rodada.setter
    def contador_rodada(self, contador_rodada):
        self.__contador_rodada = contador_rodada

    @contador_rodada.deleter
    def contador_rodada(self):
        del self.__contador_rodada
