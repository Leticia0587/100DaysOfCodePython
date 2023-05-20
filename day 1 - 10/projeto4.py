# Projeto 1 - Selecionar pessoa para pagar a refeição
nomes_string = input("Qual cartão de crédito será selecionado - até 7 pessoas: ")
nomes = nomes_string.split(", ")

numero_itens = len(nomes)

import random
random_chances = random.randint(0, numero_itens - 1)
quem_pagara = nomes[random_chances]

print(quem_pagara + " é quem pagará a refeição hoje!")

# Projeto 2 - Selecionar emoji para representar o estado de humor
row1 = ["🥰", "🙁", "😖"]
row2 = ["😬", "😔", "🤧"]
row3 = ["🥳", "🤓", "😮"]

mapa = [row1, row2, row3]
print("     1     2     3")
print(f"1 {row1[0]}   {row1[1]}   {row1[2]}")
print(f"2 {row2[0]}   {row2[1]}   {row2[2]}")
print(f"3 {row3[0]}   {row3[1]}   {row3[2]}")

posicao = input("Qual emoji representa seu estado de humor hoje? ")

if len(posicao) == 2:
    linha = int(posicao[0]) - 1
    coluna = int(posicao[1]) - 1

    if linha >= 0 and linha < 3 and coluna >= 0 and coluna < 3:
        mapa[linha][coluna] = "✅"
        print(f"{row1}\n{row2}\n{row3}")
    else:
        print("Posição inválida!")
else:
    print("Resposta inválida!")