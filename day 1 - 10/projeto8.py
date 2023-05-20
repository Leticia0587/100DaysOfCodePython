alfabeto = 'abcdefghijklmnopqrstuvwxyz'

direcao = input("Digite 'codificar' para criptografar ou 'decodificar' para descriptografar: ")
texto = input("Digite sua mensagem: ").lower()
deslocamento = int(input("Digite o número de deslocamento: "))

def caesar(texto_inicial, quantidade_de_deslocamento, direcao_da_cifra):
    fim_texto = ""
    if direcao_da_cifra == "decodificar":
        quantidade_de_deslocamento *= -1

    for letra in texto_inicial:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            nova_posicao = (indice + quantidade_de_deslocamento) % len(alfabeto)
            fim_texto += alfabeto[nova_posicao]
        else:
            fim_texto += letra
    
    print(f"Aqui está o resultado {direcao_da_cifra}: {fim_texto}")

caesar(texto, deslocamento, direcao)
