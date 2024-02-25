import pygame

class Tile:
    def __init__(self, position, tile_size, board_surface):
        self.board_surface = board_surface
        self.position = position
        self.tile_surface = pygame.Surface(tile_size)
        self.tile_surface.fill("White")

        self.board_surface.blit(self.tile_surface, position)
