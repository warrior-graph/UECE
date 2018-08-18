from abc import ABCMeta


class Elemento(metaclass=ABCMeta):
    # Atributo que representa o nome de um objeto elemento
    __nome = ""
    # Atributo que representa o nome
    __tipo_elemento = None

    def __init__(self, nome="", tipo_elemento=None):
        self.__nome = nome
        self.__tipo_elemento = tipo_elemento

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @nome.deleter
    def nome(self):
        del self.__nome

    @property
    def tipo_elemento(self):
        return self.__tipo_elemento

    @tipo_elemento.setter
    def tipo_elemento(self, tipo_elemento):
        self.__tipo_elemento = tipo_elemento

    @tipo_elemento.deleter
    def tipo_elemento(self):
        del self.__tipo_elemento
