from acao_invalida_exception import AcaoInvalidaException
from elemento import Elemento
from movimento import Movimento
from abc import ABCMeta
from tipo_elemento import TipoElemento
import random
from obstaculo import Obstaculo
from eresistencia import Eresistencia


class Animal(Elemento, metaclass=ABCMeta):
    #O atributo hp representa os pontos de vida do animal
    __hp = 0
    #O atributo bool_vivo representa o estado do animal, se esta morto ou vivo
    __bool_vivo = True


    def __init__(self, nome="", tipo_elemento=None, hp=0):
        super().__init__(nome, tipo_elemento)
        self.__hp = hp

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp):
        self.__hp = hp

    @hp.deleter
    def hp(self):
        del self.__hp

    @property
    def rato_vivo(self):
        return self.__bool_vivo

    @rato_vivo.setter
    def rato_vivo(self, bool_vivo):
        self.__bool_vivo = bool_vivo

    @rato_vivo.deleter
    def rato_vivo(self):
        del self.__bool_vivo
    # O metodo mover recebe os objetos sala e movimento como parametro. Verifica se o objeto da classe Gato ou
    # Rato(subclasses de Animal), tem pontos de vida(HP) maior que zero, caso contrario, o animal esta morto
    # e nao se movimenta. Quando o animal tentar se movimentar, a posicao possivel de movimento é verificada
    # para ser tratada as excessoes

    def mover(self, sala, movimento):

        from rato import Rato
        global linha_atual, linha_atual, coluna_atual, mensagem
        # verifica o HP do animal
        if self.hp > 0:
            self.hp -= 1
            print(self.nome + " vai tentar se mover")
            if sala.gato.contador_rodada in range(0, 3) and sala.gato.estado is "acordado":
                sala.gato.contador_rodada += 1
            else:
                sala.gato.estado = "dormindo"
                sala.gato.contador_rodada = 0
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
            linha_gato =0
            coluna_gato =0
            for i in sala.cenario:
                for j in i:
                    if j is sala.gato.tipo_elemento:
                        linha_gato = sala.cenario.index(i)
                        coluna_gato = i.index(j)
            # tenta se mover e trata todas as excecoes instruidas
            try:
                # primeiro verificamos se o objeto Rato esta nas condicoes de fazer o movimento especial, caso sim, ele
                # pula as casas e vai direto para o queijo
                # Caso nao seja um rato, e' executado um movimento comum

                if linha_nova in range(0, len(sala.cenario)) and coluna_nova in range(0, len(sala.cenario)):
                    if isinstance(self, Rato):
                        #verifica se o rato esta ao redor do gato ou vice-versa e se o gato tiver acordado, ele vai para cima do rato
                        if sala.gato.estado is "acordado":
                            if linha_atual + 1 in range(0, len(sala.cenario)) and coluna_atual + 1 in range(0, len(sala.cenario)):
                                if linha_atual - 1 in range(0, len(sala.cenario)) and coluna_atual - 1 in range(0, len(sala.cenario)):
                                    if sala.cenario[linha_atual + 1][coluna_atual] is sala.gato.tipo_elemento:
                                        sala.rato.hp = 0
                                        sala.cenario[linha_atual][coluna_atual] = sala.gato.tipo_elemento
                                        sala.cenario[linha_atual + 1][coluna_atual] = TipoElemento.Espaco_Vazio.value
                                        sala.rato.rato_vivo = False
                                        return
                                    elif sala.cenario[linha_atual - 1][coluna_atual] is sala.gato.tipo_elemento:
                                        sala.rato.hp = 0
                                        sala.cenario[linha_atual][coluna_atual] = sala.gato.tipo_elemento
                                        sala.cenario[linha_atual - 1][coluna_atual] = TipoElemento.Espaco_Vazio.value
                                        sala.rato.rato_vivo = False
                                        return
                                    elif sala.cenario[linha_atual][coluna_atual + 1] is sala.gato.tipo_elemento:
                                        sala.rato.hp = 0
                                        sala.cenario[linha_atual][coluna_atual] = sala.gato.tipo_elemento
                                        sala.cenario[linha_atual - 1][coluna_atual + 1] = TipoElemento.Espaco_Vazio.value
                                        sala.rato.rato_vivo = False
                                        return
                                    elif sala.cenario[linha_atual][coluna_atual - 1] is sala.gato.tipo_elemento:

                                        sala.rato.hp = 0
                                        sala.cenario[linha_atual][coluna_atual] = sala.gato.tipo_elemento
                                        sala.cenario[linha_atual - 1][coluna_atual - 1] = TipoElemento.Espaco_Vazio.value
                                        sala.rato.rato_vivo = False
                                        return


                        elif self.peso_adicional == 0:
                            if linha_atual == len(sala.cenario) - 3 and coluna_atual == len(sala.cenario) - 1:
                                if sala.cenario[len(sala.cenario) - 2][len(sala.cenario) - 1] is TipoElemento.Espaco_Vazio:
                                    sala.cenario[linha_atual][coluna_atual] = TipoElemento.Espaco_Vazio.value
                                    sala.cenario[len(sala.cenario) - 1][len(sala.cenario) - 1] = self.tipo_elemento

                                    if sala.rato.tenho_queijo(sala):
                                        print("Achei o queijo")
                                    sala.vizualizar_cenario()
                                    return

                            elif linha_atual == len(sala.cenario) - 1 and coluna_atual == len(sala.cenario) - 3:
                                if sala.cenario[len(sala.cenario) - 1][len(sala.cenario) - 2] is TipoElemento.Espaco_Vazio:
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

                        lista_movimento = []
                        lista_movimento.append(Movimento.up.value)
                        lista_movimento.append(Movimento.down.value)
                        lista_movimento.append(Movimento.left.value)
                        lista_movimento.append(Movimento.right.value)

                        if movimento is Movimento.up.value:
                            sala.gato.mover(sala, Movimento.down.value)
                            if sala.rato.hp > 0:
                                sala.rato.mover(sala, random.choice(lista_movimento))
                            else:
                                return
                            sala.gato.mover(sala, Movimento.down.value)

                        elif movimento is Movimento.down.value:
                            sala.gato.mover(sala, Movimento.up.value)
                            if sala.rato.hp > 0:
                                sala.rato.mover(sala, random.choice(lista_movimento))
                            else: return
                            sala.gato.mover(sala, Movimento.up.value)

                        elif movimento is Movimento.right.value:
                            sala.gato.mover(sala, Movimento.left.value)
                            if sala.rato.hp > 0:
                                sala.rato.mover(sala, random.choice(lista_movimento))
                            else:
                                return
                            sala.gato.mover(sala, Movimento.left.value)

                        elif movimento is Movimento.left.value:
                            sala.gato.mover(sala, Movimento.right.value)
                            if sala.rato.hp > 0:
                                sala.rato.mover(sala, random.choice(lista_movimento))
                            else:
                                return
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

    
