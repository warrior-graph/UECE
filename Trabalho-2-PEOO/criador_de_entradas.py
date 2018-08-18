#Este deve ser o primeiro modulo executado para gerar os arquivos de textos a serem lidos pela main
lista = ["7\n", "6x3\n", "5\n", "5x5 Fragil\n", "5x4 Resistente\n", "4x2 Fragil\n", "3x1 Resistente\n", "2x2 Resistente\n"]

with open("Entrada1.txt", "w") as file:
    file.writelines(lista)

lista = ["7\n", "4x5\n", "5\n", "6x5 Fragil\n", "5x2 Resistente\n", "3x1 Resistente\n", "3x4 Resistente\n", "1x1 Fragil\n"]

with open("Entrada2.txt", "w") as file:
    file.writelines(lista)

lista = ["7\n", "3x6\n", "5\n", "4x5 Resistente\n", "5x4 Fragil\n", "3x3 Resistente\n", "2x2 Fragil\n", "1x1 Resistente\n"]

with open("Entrada3.txt", "w") as file:
    file.writelines(lista)
