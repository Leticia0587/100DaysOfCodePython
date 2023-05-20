import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

def choose_word(word_list):
    return random.choice(word_list)

def display_word(word, guesses):
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman():
    print(logo)
    chosen_word = choose_word(word_list)
    word_length = len(chosen_word)
    guessed_letters = []
    game_over = False
    lives = len(stages) - 1

    while not game_over:
        guess = input("Escolha uma letra: ").lower()
        clear()

        if guess in guessed_letters:
            print(f"Você já adivinhou a letra '{guess}'.")

        guessed_letters.append(guess)
        word_display = display_word(chosen_word, guessed_letters)
        print(word_display)

        if guess not in chosen_word:
            print(f"A letra '{guess}' não está na palavra. Você perdeu uma vida.")
            lives -= 1
            if lives == 0:
                game_over = True
                print("Você perdeu o jogo.")
                print(f"A palavra era '{chosen_word}'.")
        elif "_" not in word_display:
            game_over = True
            print("Parabéns! Você venceu o jogo.")

        print(stages[lives])

    play_again = input("Deseja jogar novamente? (s/n): ").lower()
    if play_again == "s":
        clear()
        hangman()
    else:
        print("Obrigado por jogar o jogo da Forca!")

hangman()
