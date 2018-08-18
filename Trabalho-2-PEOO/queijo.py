from elemento import Elemento


class Queijo(Elemento):
    # Atributo que representa o peso de um objeto Queijo
    __peso = 0

    def __init__(self, peso=0, nome="", tipo_elemento=None):
        super().__init__(nome, tipo_elemento)
        self.__peso = peso

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @peso.deleter
    def peso(self):
        del self.__peso
