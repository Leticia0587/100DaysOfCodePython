print("Bem vindo a ilha do Tesouro.")
print("Sua missão é encontrar o tesouro.")
choice1 = input('Você está em uma encruzilhada, para onde deseja ir? Digite "esquerda" ou "direita".\n').lower()

if choice1 == "esquerda":
    choice2 = input('Você chegou a um lago. Há uma ilha no meio do lago. Digite "wait" para esperar um barco. Digite "swim" para atravessar nadando .\n').lower()
    if choice2 == "wait":
        choice3 = input("Você chega ileso à ilha. Há uma casa com 3 portas. Uma vermelha, uma amarela e uma azul. Qual cor você escolhe.\n").lower()
        if choice3 == "vermelha":
            print("É uma sala cheia de fogo. Fim do jogo")
        elif choice3 == "amarelo":
            print("Você encontrou o tesouro! Você Ganhou!")
        elif choice3 == "azul":
            print("Você entra em uma sala cheia de feras. Fim de jogo.")
        else:
            print("Você escolheu uma porta que não existe. Fim do jogo.")
    else:
      print("Você foi atacado por um bicho furioso. Fim de jogo.")
else:
    print("Você caiu em um buraco. Fim do jogo")