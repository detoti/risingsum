from ball import Ball

class Computer:
    def __init__(self):
        self.target = Ball.draw()

    def generate_target(self):
        new_ball = Ball.draw()
        self.target = Ball(self.target.number + new_ball.number)