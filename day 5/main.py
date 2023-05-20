# For Loop with Lists
frutas = ["Maça", "Uva", "Perá"]

# Loop que itera sobre os elementos da lista "frutas"
for fruta in frutas:
    # Imprime o valor da fruta
    print(fruta)
    # Imprime o valor da fruta seguido da string "cortada"
    print(fruta + " cortada")

# For Loop with Range

# Loop que itera sobre uma sequência de números de 1 a 19
for numero in range(1, 20):
    # Imprime o valor do número
    print(numero)

# Loop que itera sobre uma sequência de números de 1 a 99
for numero in range(1, 100):
    # Imprime o valor do número
    print(numero)

# Loop que itera sobre uma sequência de números de 1 a 100
for numero in range(1, 101):
    # Imprime o valor do número
    print(numero)

# Loop que itera sobre uma sequência de números de 1 a 10 com passo 3
for numero in range(1, 11, 3):
    # Imprime o valor do número
    print(numero)

# Calculando a soma de todos os números de 1 a 100.
total = 0

# Loop que itera sobre uma sequência de números de 1 a 100
for numero in range(1, 101):
    # Adiciona o valor do número à variável "total"
    total += numero

# Imprime o valor total
print(total)
