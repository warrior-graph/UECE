import xml.etree.ElementTree as ET
from decimal import Decimal
from metodos import Metodos
import os as check_arquivo


class Usuario(Metodos):
    __matricula = ""
    __nome = ""
    __debito = 0
    __tipo = ""
    __pagina = 1
    __matricula_seq = 1
    __tem_matricula = False

    def __init__(self, nome="", debito=0, tipo="", tem_matricula = False):
        self.__nome = nome
        self.__debito = debito
        self.__tipo = tipo
        self.__tem_matricula = tem_matricula


    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @matricula.deleter
    def matricula(self):
        del self.__matricula

    def inserir(self):

        nome_do_arquivo = "usuario" + "_" + self.__nome[0].capitalize() + str(self.__pagina) + ".xml"
        root = self.ler_arquivo_xml(nome_do_arquivo)
        if root is None:
            root = ET.Element('root')
            tree = ET.ElementTree(root)
            tree.write(nome_do_arquivo)
        contador = 0
        for i in root.findall('usuario'):
            contador += 1
            if "-25-" in i.find('matricula').text:
                contador = 25

        if contador == 25:
            self.__pagina += 1
            self.inserir()
            return
        else:
            self.__matricula_seq = str(contador + 1) + '-' + str(self.__pagina)
        if not self.__tem_matricula:
            self.__matricula = str(ord(self.__nome[0].lower()) - 96) + '-' + self.__matricula_seq

        usuario = ET.SubElement(root, 'usuario')
        ET.SubElement(usuario, 'matricula').text = self.__matricula
        ET.SubElement(usuario, 'nome').text = self.__nome
        ET.SubElement(usuario, 'debito').text = str(self.__debito)
        ET.SubElement(usuario, 'tipo').text = self.__tipo

        ET.ElementTree(root).write(nome_do_arquivo)

    def remover(self, matricula):
        numero_elementos = 0
        nome_do_arquivo = self.pesquisar(matricula=matricula, printar=False)
        if nome_do_arquivo is None:
            print("Inexistente")
            return
        else:
            root = self.ler_arquivo_xml(nome_do_arquivo)

        for usr in root.findall('usuario'):
            if usr.find('matricula').text == matricula:
                root.remove(usr)
        for i in root.findall('usuario'):
            numero_elementos += 1
        if numero_elementos > 0:
            ET.ElementTree(root).write(nome_do_arquivo)
        else:
            check_arquivo.remove(nome_do_arquivo)

    def pesquisar(self, matricula=None, nome=None, printar=True):
        arq_num = 0
        if matricula is None and nome is None:
            if printar:
                print("Insira nome ou matricula para fazer uma pesquisa...")
        if matricula is not None:
            while True:
                arq_num += 1
                if matricula[1] == '-':
                    nome_do_arquivo = "usuario_" + chr(int(matricula[0]) + 96).capitalize() + str(arq_num) + ".xml"
                else:
                    nome_do_arquivo = "usuario_" + chr(int(matricula[0] + matricula[1]) + 96).capitalize() \
                                      + str(arq_num) + ".xml"
                if check_arquivo.path.isfile(nome_do_arquivo):
                    root = self.ler_arquivo_xml(nome_do_arquivo)
                    for usr in root.findall('usuario'):
                        if usr.find('matricula').text == matricula:
                            if printar:
                                print("Nome:", usr.find('nome').text)
                                print("Matricula:", usr.find('matricula').text)
                                print("Tipo:", usr.find('tipo').text)
                            return nome_do_arquivo
                else:
                    if printar:
                        print("Nao encontrado")
                    return None
        elif nome is not None:
            while True:
                arq_num += 1
                nome_do_arquivo = "usuario_" + nome[0].capitalize() + str(arq_num) + ".xml"
                if check_arquivo.path.isfile(nome_do_arquivo):
                    root = self.ler_arquivo_xml(nome_do_arquivo)
                    for usr in root.findall('usuario'):
                        if usr.find('nome').text == nome:
                            if printar:
                                print("Nome:", usr.find('nome').text)
                                print("Matricula:", usr.find('matricula').text)
                                print("Tipo:", usr.find('tipo').text)
                else:
                    if printar:
                        print("Nao encontrado")
                    return None

    def alterar(self, matricula=None, nome=None, tipo=None):
        nome_alterado = ""
        tipo_alterado = ""
        debito = ""
        nome_do_arquivo = self.pesquisar(matricula=matricula, printar=False)
        if nome_do_arquivo is None or matricula is None or (nome is None and tipo is None):
            print("Inalterado")
            return
        else:
            root = self.ler_arquivo_xml(nome_do_arquivo)
        if nome is not None and tipo is not None:
            for usr in root.findall('usuario'):
                if usr.find('matricula').text == matricula:
                    debito = usr.find('debito').text
                    usuario_alterado = Usuario(nome, debito, tipo)
                    usuario_alterado.inserir()
        elif nome is None:
            for usr in root.findall('usuario'):
                if usr.find('matricula').text == matricula:
                    debito = usr.find('debito').text
                    nome_alterado = usr.find('nome').text
                    usuario_alterado = Usuario(nome_alterado, debito, tipo)
                    usuario_alterado.inserir()

        elif tipo is None:
            for usr in root.findall('usuario'):
                if usr.find('matricula').text == matricula:
                    debito = usr.find('debito').text
                    tipo_alterado = usr.find('tipo').text
                    usuario_alterado = Usuario(nome, debito, tipo_alterado)
                    usuario_alterado.inserir()
        print("Nova matricula:", usuario_alterado.matricula)
        ET.ElementTree(root).write(nome_do_arquivo)
        self.remover(matricula)

    def listar(self, arquivo_xml):
        root = self.ler_arquivo_xml(arquivo_xml)

        for usr in root.findall('usuario'):
            print("Tipo:", usr.find('tipo').text)
            print("Nome:", usr.find('nome').text)
            print("Matricula:", usr.find('matricula').text)
            print("Debito:", usr.find('debito').text)

    def debitar(self, arquivo_xml, matricula=None, saldar=None):
        matricula_finder = self.pesquisar(arquivo_xml, matricula, printar=False)
        if matricula_finder is None:
            print("Nada foi debitado")
            return
        root = self.ler_arquivo_xml(arquivo_xml)

        for usuario in root.findall('usuario'):
            if usuario.find('matricula').text == matricula_finder:
                if saldar is None:
                    root.findall('usuario')[root.findall('usuario').index(usuario)].find('debito').text = '0'
                else:
                    root.findall('usuario')[root.findall('usuario').index(usuario)].find('debito').text = \
                        str(Decimal(usuario.find('debito').text) - saldar)
        ET.ElementTree(root).write(arquivo_xml)

