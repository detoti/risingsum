class Game:
    def __init__(self, computer):
        self.computer = computer

    def check_guess(self, guess):
        if guess == self.computer.target.number:
            return True
        else:
            return False

    def check_target(self):
        if self.computer.target.number == 100:
            return "Computer"
        elif self.computer.target.number > 100:
            return "User"
        else:
            return None