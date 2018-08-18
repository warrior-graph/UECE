import random

from acao_invalida_exception import AcaoInvalidaException
from animal import Animal
from eresistencia import Eresistencia
from movimento import Movimento
from obstaculo import Obstaculo
from tipo_elemento import TipoElemento


class Rato(Animal):
    #Atributo que representa o peso de um objeto Rato
    __peso = 0
    #Atributo que representa o peso adicional de um objeto Rato
    __peso_adicional = 0
    #Atributo que representa um objeto arquivo da memoria do Rato
    __memoria = None
    #nome do arquivo
    __nome_do_arquivo = ""


    def __init__(self, peso=0, peso_adicional=0, hp=0, nome="", tipo_elemento=None, nome_do_arquivo=""):
        super().__init__(nome, tipo_elemento, hp)
        self.__peso = peso
        self.__peso_adicional = peso_adicional
        self.__nome_do_arquivo = nome_do_arquivo

    @property
    def nome_do_arquivo(self):
        return self.__nome_do_arquivo

    @nome_do_arquivo.setter
    def nome_do_arquivo(self, nome_do_arquivo):
        self.__nome_do_arquivo = nome_do_arquivo

    @nome_do_arquivo.deleter
    def nome_do_arquivo(self):
        del self.__nome_do_arquivo

    @property
    def memoria(self):
        return self.__memoria

    @memoria.setter
    def memoria(self, memoria):
        self.__memoria = memoria

    @memoria.deleter
    def memoria(self):
        del self.__memoria

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


    def mover(self, sala, movimento):

        from rato import Rato
        global linha_atual, linha_atual, coluna_atual, mensagem
        # verifica o HP do animal
        if self.hp > 0:
            self.hp -= 1
            if sala.gato.contador_rodada in range(0, 3) and sala.gato.estado is "acordado":
                sala.gato.estado = "acprdado"
                sala.gato.contador_rodada += 1
            else:
                sala.gato.estado = "dormindo"
                sala.gato.contador_rodada = 0

            print(self.nome + " vai tentar se mover")
            # pesquisa o elemento a ser movimentado
            for i in sala.cenario:
                for j in i:
                    if j is self.tipo_elemento:
                        linha_atual = sala.cenario.index(i)
                        coluna_atual = i.index(j)
                        print("Posicao que tava")
                        print(linha_atual + 1, coluna_atual + 1)

            linha_nova = linha_atual
            coluna_nova = coluna_atual

            if movimento is Movimento.up.value:
                linha_nova = linha_atual - 1
            elif movimento is Movimento.down.value:
                linha_nova = linha_atual + 1
            elif movimento is Movimento.right.value:
                coluna_nova = coluna_atual + 1
            elif movimento is Movimento.left.value:
                coluna_nova = coluna_atual - 1

            # tenta se mover e trata todas as excecoes instruidas
            try:
                # primeiro verificamos se o objeto Rato esta nas condicoes de fazer o movimento especial, caso sim, ele
                # pula as casas e vai direto para o queijo
                # Caso nao seja um rato, e' executado um movimento comum
                if linha_nova in range(0, len(sala.cenario)) and coluna_nova in range(0, len(sala.cenario)):
                    if sala.gato.estado is "acordado":
                        if linha_atual + 1 in range(0, len(sala.cenario)) and coluna_atual + 1 in range(0, len(
                                sala.cenario)):
                            if linha_atual - 1 in range(0, len(sala.cenario)) and coluna_atual - 1 in range(0, len(
                                    sala.cenario)):
                                if sala.cenario[linha_atual + 1][coluna_atual] is sala.gato.tipo_elemento:
                                    print(sala.gato.nome, " diz: Estou com fome!!!")
                                    sala.rato.hp = 0
                                    sala.cenario[linha_atual][coluna_atual] = sala.gato.tipo_elemento
                                    sala.cenario[linha_atual + 1][coluna_atual] = TipoElemento.Espaco_Vazio.value
                                    sala.rato.rato_vivo = False
                                    return
                                elif sala.cenario[linha_atual - 1][coluna_atual] is sala.gato.tipo_elemento:
                                    print(sala.gato.nome, " diz: Estou com fome!!!")
                                    sala.rato.hp = 0
                                    sala.cenario[linha_atual][coluna_atual] = sala.gato.tipo_elemento
                                    sala.cenario[linha_atual - 1][coluna_atual] = TipoElemento.Espaco_Vazio.value
                                    sala.rato.rato_vivo = False
                                    return
                                elif sala.cenario[linha_atual][coluna_atual + 1] is sala.gato.tipo_elemento:
                                    print(sala.gato.nome, " diz: Estou com fome!!!")
                                    sala.rato.hp = 0
                                    sala.cenario[linha_atual][coluna_atual] = sala.gato.tipo_elemento
                                    sala.cenario[linha_atual - 1][coluna_atual + 1] = TipoElemento.Espaco_Vazio.value
                                    sala.rato.rato_vivo = False
                                    return
                                elif sala.cenario[linha_atual][coluna_atual - 1] is sala.gato.tipo_elemento:
                                    print(sala.gato.nome, " diz: Estou com fome!!!")
                                    sala.rato.hp = 0
                                    sala.cenario[linha_atual][coluna_atual] = sala.gato.tipo_elemento
                                    sala.cenario[linha_atual - 1][coluna_atual - 1] = TipoElemento.Espaco_Vazio.value
                                    sala.rato.rato_vivo = False
                                    return

                    #aqui o arquivo é lido, se a posicao a se mover estiver no arquivo de texto da memoria
                    #o rato pula para o proximo movimento
                    with open(self.nome_do_arquivo, "r") as file_search:
                        data = file_search.readlines()
                        posicao = str(linha_nova) + "x" + str(coluna_nova) + '\n'
                        if posicao in data:
                            return


                    if self.peso_adicional == 0:
                        if linha_atual == len(sala.cenario) - 3 and coluna_atual == len(sala.cenario) - 1:
                            if sala.cenario[len(sala.cenario) - 2][
                                        len(sala.cenario) - 1] is TipoElemento.Espaco_Vazio:
                                sala.cenario[linha_atual][coluna_atual] = TipoElemento.Espaco_Vazio.value
                                sala.cenario[len(sala.cenario) - 1][len(sala.cenario) - 1] = self.tipo_elemento

                                if sala.rato.tenho_queijo(sala):
                                    print("Achei o queijo")
                                sala.vizualizar_cenario()
                                return

                        elif linha_atual == len(sala.cenario) - 1 and coluna_atual == len(sala.cenario) - 3:
                            if sala.cenario[len(sala.cenario) - 1][
                                        len(sala.cenario) - 2] is TipoElemento.Espaco_Vazio:
                                sala.cenario[linha_atual][coluna_atual] = TipoElemento.Espaco_Vazio.value
                                sala.cenario[len(sala.cenario) - 1][len(sala.cenario) - 1] = self.tipo_elemento

                                if sala.rato.tenho_queijo(sala):
                                    print("Achei o queijo")
                                sala.vizualizar_cenario()
                                return

                        elif linha_atual == len(sala.cenario) - 2 and coluna_atual == len(sala.cenario) - 1:
                            sala.cenario[linha_atual][coluna_atual] = TipoElemento.Espaco_Vazio.value
                            sala.cenario[len(sala.cenario) - 1][len(sala.cenario) - 1] = self.tipo_elemento

                            if sala.rato.tenho_queijo(sala):
                                print("Achei o queijo")
                            sala.vizualizar_cenario()
                            return

                        elif linha_atual == len(sala.cenario) - 1 and coluna_atual == len(sala.cenario) - 2:
                            sala.cenario[linha_atual][coluna_atual] = TipoElemento.Espaco_Vazio.value
                            sala.cenario[len(sala.cenario) - 1][len(sala.cenario) - 1] = self.tipo_elemento

                            if sala.rato.tenho_queijo(sala):
                                print("Achei o queijo")
                            sala.vizualizar_cenario()
                            return

                    if sala.cenario[linha_nova][coluna_nova] is sala.rato.tipo_elemento:
                        sala.rato.hp = 0
                        sala.cenario[linha_nova][coluna_nova] = self.tipo_elemento
                        sala.cenario[linha_atual][coluna_atual] = TipoElemento.Espaco_Vazio.value
                        sala.rato.rato_vivo = False
                        return

                    elif sala.cenario[linha_nova][coluna_nova] is TipoElemento.Espaco_Vazio.value:
                        sala.cenario[linha_atual][coluna_atual] = TipoElemento.Espaco_Vazio.value
                        sala.cenario[linha_nova][coluna_nova] = self.tipo_elemento

                        print(self.nome + " se moveu")
                    elif sala.cenario[linha_nova][coluna_nova] is TipoElemento.Gato.value:
                        movimentos = [Movimento.up.value, Movimento.down.value, Movimento.right.value,
                                      Movimento.left.value]
                        movimento_randomico = random.choice(movimentos)

                        print("Fugindo")
                        if movimento_randomico is not movimento:
                            self.mover(sala, movimento_randomico)
                        else:
                            self.mover(sala, movimento)

                    elif isinstance(sala.cenario[linha_nova][coluna_nova], Obstaculo):
                        print("Memorizei")
                        posicao = str(linha_nova) + "x" + str(coluna_nova) + '\n'
                        with open(self.nome_do_arquivo, "r") as file_search:
                            data = file_search.readlines()
                            if posicao not in data:
                                with open(self.nome_do_arquivo, "a") as file:
                                    file.write(posicao)
                                    self.__memoria = file

                        if sala.cenario[linha_nova][coluna_nova].resistencia is Eresistencia.fragil:
                            sala.cenario[linha_nova][coluna_nova] = TipoElemento.Espaco_Vazio.value
                            movimentos = [Movimento.up.value, Movimento.down.value,
                                          Movimento.right.value, Movimento.left.value]
                            movimento_randomico = random.choice(movimentos)
                            self.mover(sala, movimento_randomico)

                        mensagem = 1
                        raise AcaoInvalidaException
                else:
                    mensagem = 2
                    raise AcaoInvalidaException

            except AcaoInvalidaException as invalidez:
                if mensagem == 1:
                    if isinstance(self, Rato):
                        if sala.gato.hp == 0:
                            print("O gato morreu")
                            sala.vizualizar_cenario()
                            return
                        sala.gato.estado = "acordado"

                        if sala.gato.contador_rodada <= 2:
                            print("O gato esta: " + sala.gato.estado)
                        else:
                            sala.gato.contador_rodada = 0
                            sala.gato.estado = "dormindo"
                            print("O gato esta:", sala.gato.estado)

                        lista_movimento = []
                        lista_movimento.append(Movimento.up.value)
                        lista_movimento.append(Movimento.down.value)
                        lista_movimento.append(Movimento.left.value)
                        lista_movimento.append(Movimento.right.value)

                        if sala.rato.hp > 0:
                            if movimento is Movimento.up.value:
                                sala.gato.mover(sala, Movimento.down.value)
                                sala.rato.mover(sala, random.choice(lista_movimento))
                                sala.gato.mover(sala, Movimento.down.value)

                            elif movimento is Movimento.down.value:
                                sala.gato.mover(sala, Movimento.up.value)
                                sala.rato.mover(sala, random.choice(lista_movimento))
                                sala.gato.mover(sala, Movimento.up.value)

                            elif movimento is Movimento.right.value:
                                sala.gato.mover(sala, Movimento.left.value)
                                sala.rato.mover(sala, random.choice(lista_movimento))
                                sala.gato.mover(sala, Movimento.left.value)

                            elif movimento is Movimento.left.value:
                                sala.gato.mover(sala, Movimento.right.value)
                                sala.rato.mover(sala, random.choice(lista_movimento))
                                sala.gato.mover(sala, Movimento.right.value)
                        else:
                            return
                    invalidez.obstaculo(self.nome)
                elif mensagem == 2:
                    invalidez.extrapolar(self.nome)
        else:
            print(self.nome, " esta morto!")
            return
        sala.vizualizar_cenario()

    def mover_gato(sala):
        pass
