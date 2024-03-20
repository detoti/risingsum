# Main.py
from computer import Computer
from game import Game
from retry import Retry
from kick import Kick

computer = Computer()
game = Game(computer)

while True:
    guess_number = int(input("Digite seu palpite: "))
    guess = Kick(guess_number)
    
    if game.check_guess(guess):
        print("Parabéns! Você acertou o alvo.")
        break
    else:
        print("Você errou! Tente novamente.")
        computer.generate_target()
        
    winner = game.check_target()
    if winner == "Computer":
        print("O alvo ultrapassou 100. O computador venceu!")
        break
    elif winner == "User":
        print("O alvo ultrapassou 100. Você perdeu!")
        break

    play_again = Retry.try_again()
    if play_again.upper() != "S":
        break
