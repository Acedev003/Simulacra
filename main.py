import pygame


def init():
    pass

def update():
    pass

def draw():
    pass

class Game:
    def __init__(self):
        pygame.init()
        self.screen  = pygame.display.set_mode((1280, 720))
        self.clock   = pygame.time.Clock()
        self.running = True

    def update(self):
        pass

    def draw(self):
        pass

    def run(self):
        while self.running:            
            self.update()
            self.draw()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()
