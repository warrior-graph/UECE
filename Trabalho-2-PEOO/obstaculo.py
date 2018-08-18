from tipo_elemento import TipoElemento
from elemento import Elemento

#classe que repressenta um obstaculo
class Obstaculo(Elemento):
    #atributo que representa um numerador eresistencia
    __resistecia = None

    def __init__(self, nome, resistencia):
        super().__init__(nome, TipoElemento.Obstaculo.value)
        self.__resistecia = resistencia

    @property
    def resistencia(self):
        return self.__resistecia

    @resistencia.setter
    def resistencia(self, resistencia):
        self.__resistecia = resistencia

    @resistencia.deleter
    def resistencia(self):
        del self.__resistecia

