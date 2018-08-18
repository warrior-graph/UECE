from gato import Gato
from movimento import Movimento
from rato import Rato
from tipo_elemento import TipoElemento
from sala import Sala
from queijo import Queijo
import random

sala = Sala()

sala.inicializar(7)
sala.gato = Gato("Fly-Gone-Gin", TipoElemento.Gato.value, 200, "dormindo", 0)
sala.rato = Rato(120, 0, 1500, "Toby One", TipoElemento.Rato.value)
sala.queijo = Queijo(200, "coalho", TipoElemento.Queijo.value)

lista_movimento = []
lista_movimento.append(Movimento.up.value)
lista_movimento.append(Movimento.down.value)
lista_movimento.append(Movimento.left.value)
lista_movimento.append(Movimento.right.value)

while True:
    if sala.queijo.peso == 0 and sala.cenario[0][0] is sala.rato.tipo_elemento:
        break
    else:
        if sala.rato.hp == 0:
            break
        else:
            sala.rato.mover(sala, random.choice(lista_movimento))

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
