import pygame
from input import Input
from tile import Tile

class Game:
    def __init__(self, window):
        self.window = window
        self.board_surface = pygame.Surface((self.window.width, self.window.height))
        self.tiles = []
        self.tile_size = []
        self.board_size = [10, 10]
        self.border_size = 4

        self.InitializeBoard()
        self.input_handler = Input(self)

        self.hover_tile = None

    def InitializeBoard(self):
        avail_width = self.window.width - (self.border_size * (self.board_size[0] + 1))
        avail_height = self.window.height - (self.border_size * (self.board_size[1] + 1))

        self.tile_size = [(avail_width / self.board_size[0]), (avail_height / self.board_size[1])]

        for x in range(self.board_size[0]):
            for y in range(self.board_size[1]):
                border_x = 1 if x != 0 else 0
                border_y = 1 if y != 0 else 0

                tile_position = [
                    (self.border_size) + (x * (self.tile_size[0] + self.border_size * border_x)),
                    (self.border_size) + (y * (self.tile_size[1] + self.border_size * border_y)),
                ]

                tile = Tile(tile_position, self.tile_size, self.board_surface)
                self.tiles.append(tile)

        self.window.draw_surface.blit(self.board_surface, (0, 0))

    def Update(self, events):
        if len(events) > 0:
            for event in events:
                if event.type == pygame.MOUSEMOTION:
                    self.HandleHover(event)

                if event.type == pygame.WINDOWLEAVE:
                    self.HandleMouseLeave()

    def HandleHover(self, event):
        mouse_pos = event.pos
        tile_coords = (
            int((mouse_pos[0] - self.border_size) // (self.tile_size[0] + self.border_size)),
            int((mouse_pos[1] - self.border_size) // (self.tile_size[1] + self.border_size))
        )

        print(tile_coords[0] + tile_coords[1] * self.board_size[0])

        if 0 <= tile_coords[0] < self.board_size[0] and 0 <= tile_coords[1] < self.board_size[1]:
            tile_index = tile_coords[0] + tile_coords[1] * self.board_size[0]
            tile = self.tiles[tile_index]

            if tile != self.hover_tile:
                tile.SetColor(tile.tile_colors["hover"])
                if self.hover_tile:
                    self.hover_tile.SetColor(self.hover_tile.tile_colors["default"])

            self.hover_tile = tile
            print(tile)
        else:
            # Handle the case where the mouse is outside the board
            if self.hover_tile:
                self.hover_tile.SetColor(self.hover_tile.tile_colors["default"])
            self.hover_tile = None

    def HandleMouseLeave(self):
        self.hover_tile = None