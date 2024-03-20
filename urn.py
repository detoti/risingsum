class Urn:
    def __init__(self, balls):
        self.balls = balls

    def add_ball(self, ball):
        self.balls.append(ball)

    def remove_ball(self, ball):
        self.balls.remove(ball)