import pygame

from game import Game

class Window:
    def __init__(self, width, height, fps):
        pygame.init()
        # self.clock = pygame.time.Clock()

        self.running = True
        self.width = width
        self.height = height
        self.fps = fps

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("game")

        self.draw_surface = pygame.Surface((width, height))

        self.game = Game(self)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.screen.fill("Black")
        self.game.update()

        self.screen.blit(self.draw_surface, (0, 0))

        pygame.display.flip()

    def quit(self):
        pygame.quit()