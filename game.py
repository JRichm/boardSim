import pygame
from tile import Tile

class Game:
    def __init__(self, window):
        self.window = window
        self.board_surface = pygame.Surface((self.window.width, self.window.height))
        self.tiles = []
        self.board_size = [10, 10]
        self.border_size = 5

        self.initialize_board()

    def initialize_board(self):
        avail_width = self.window.width - (self.border_size * self.board_size[0])
        avail_height = self.window.height - (self.border_size * self.board_size[1])

        tile_size = ((avail_width / self.board_size[0]) - self.border_size / 2, (avail_height / self.board_size[1]) - self.border_size / 2)

        for x in range(self.board_size[0]):
            for y in range(self.board_size[1]):
                border_x = 1 if x != 0 else 0
                border_y = 1 if y != 0 else 0

                tile_position = [
                    (self.border_size) + (x * (tile_size[0] + self.border_size * border_x)),
                    (self.border_size) + (y * (tile_size[1] + self.border_size * border_y)),
                ]

                tile = Tile(tile_position, tile_size, self.board_surface)
                self.tiles.append(tile)

        self.window.draw_surface.blit(self.board_surface, (0, 0))

    def update(self):
        pass
