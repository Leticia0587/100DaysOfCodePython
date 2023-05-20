# Solução interativa para completar o desafio "Hurdle 4" no Reeborg's World
# O objetivo é fazer o robô percorrer o caminho até alcançar o objetivo,
# superando obstáculos no caminho.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Enquanto houver caminho à frente, continue movendo-se
while front_is_clear():
    move()

# Vire à esquerda
turn_left()

# Loop principal para completar o desafio
while not at_goal():
    # Se houver caminho à direita, vire à direita e mova-se
    if right_is_clear():
        turn_right()
        move()
    # Se houver caminho à frente, mova-se
    elif front_is_clear():
        move()
    # Caso contrário, vire à esquerda
    else:
        turn_left()
