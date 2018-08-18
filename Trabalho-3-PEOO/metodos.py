from abc import ABCMeta, abstractmethod
import xml.etree.ElementTree as ET


class Metodos(metaclass=ABCMeta):
    def ler_arquivo_xml(self, arquivo_xml):
        try:
            tree = ET.parse(arquivo_xml)
            root = tree.getroot()
            return root
        except FileNotFoundError:
            return None

    @abstractmethod
    def inserir(self):
        pass

    @abstractmethod
    def remover(self):
        pass

    @abstractmethod
    def pesquisar(self):
        pass

    @abstractmethod
    def alterar(self):
        pass

    @abstractmethod
    def listar(self):
        pass