import xml.etree.ElementTree as ET
from metodos import Metodos
from decimal import Decimal

class LivroHQ(Metodos):
    __isbn = ""
    __titulo = ""
    __autor = 0
    __editora = ""
    __tipo = ""

    def __init__(self, isbn="", titulo="", autor=0, tipo="", editora=""):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__tipo = tipo
        self.__editora = editora

    def ler_arquivo_xml(self, arquivo_xml):
        try:
            tree = ET.parse(arquivo_xml)
            root = tree.getroot()
            return root
        except FileNotFoundError:
            root = ET.Element('root')
            tree = ET.ElementTree(root)
            tree.write(arquivo_xml)
            return root

    def inserir(self, arquivo_xml):
        root = self.ler_arquivo_xml(arquivo_xml)
        contador = 0
        for i in root.findall('livro_hq'):
            contador += 1
        # print(contador)
        if contador == 25:
            return
        for i in root.findall('livro_hq'):
            if i.find('isbn').text == self.__isbn or i.find('isbn').text is None:
                return

        livro_hq = ET.SubElement(root, 'livro_hq')
        ET.SubElement(livro_hq, 'isbn').text = self.__isbn
        ET.SubElement(livro_hq, 'titulo').text = self.__titulo
        ET.SubElement(livro_hq, 'autor').text = self.__autor
        ET.SubElement(livro_hq, 'tipo').text = self.__tipo
        ET.SubElement(livro_hq, 'editora').text = self.__editora

        ET.ElementTree(root).write(arquivo_xml)

    def remover(self, arquivo_xml, isbn):
        root = self.ler_arquivo_xml(arquivo_xml)
        for lhq_finder in root.findall('livro_hq'):
            if lhq_finder.find('isbn').text == isbn:
                root.remove(lhq_finder)
        ET.ElementTree(root).write(arquivo_xml)

    def pesquisar(self, arquivo_xml,):
        pass
    def alterar(self):
        pass
    def listar(self):
        pass