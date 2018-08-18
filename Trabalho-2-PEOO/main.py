from gato import Gato
from movimento import Movimento
from rato import Rato
from tipo_elemento import TipoElemento
from sala import Sala
from queijo import Queijo
import random


sala = Sala()
#depois de executar o modulo
sala.inicializar("Entrada1.txt")

sala.gato = Gato("Fly-Gone-Gin", TipoElemento.Gato.value, 15, "dormindo", 0)
sala.rato = Rato(50, 0, 2000, "Toby One", TipoElemento.Rato.value, "memoria_do_rato.txt")
sala.queijo = Queijo(200, "coalho", TipoElemento.Queijo.value)

lista_movimento = []
lista_movimento.append(Movimento.up.value)
lista_movimento.append(Movimento.down.value)
lista_movimento.append(Movimento.left.value)
lista_movimento.append(Movimento.right.value)

#apaga a memoria do rato toda vez que o programa e' executado
sala.rato.memoria = open("memoria_do_rato.txt", "w")
sala.rato.memoria.write("")
i = 0
while True:
    if sala.queijo.peso == 0 and sala.cenario[0][0] is sala.rato.tipo_elemento:
        break
    else:
        if sala.rato.hp == 0:
            break
        else:
            sala.rato.mover(sala, random.choice(lista_movimento))
            i += 1

            sala.rato.carregar(sala)
            sala.rato.descarregar(sala)
            print("Queijo restante: ", sala.queijo.peso, "g")


#Se o rato morrer pelas patas do gato, ainda sera executado 2 prints pois o gato deve se mover 2 vezes
#e' so pra o senhor nao pensar que seja um bug do rato sumir
print("\n\nRESULTADO FINAL")
print("#####################################################################################################")
sala.vizualizar_cenario()
print(sala.rato.nome, "HP: ", sala.rato.hp)
print(sala.gato.nome, "HP: ", sala.gato.hp)
if sala.rato.hp == 0:
    print(sala.rato.nome, " morreu...")
    if not sala.rato.rato_vivo:
        print(sala.rato.nome, "nao conseguiu sobreviver ao imponente", sala.gato.nome)
if sala.gato.hp == 0:
    print(sala.gato.nome, " morreu...")

