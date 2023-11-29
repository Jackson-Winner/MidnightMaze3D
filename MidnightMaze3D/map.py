import pygame as pg
import math


# Create the map as list of lists. An underscore (_) is open space and positive values are walls of a certain texture
_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1, 1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1, 1, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, 1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, 1, _, _, 1, 1, 1, _, _, _, 1],
    [1, _, _, 1, _, _, 1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, 1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, 1, _, _, _, 1, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.rows = len(self.mini_map)
        self.cols = len(self.mini_map[0])
        self.get_map()

    # This functions goes through minimap which is a list of lists, and enumerates all the rows and for every one
    # of those rows it enumerates all the columns in that row and if that grid squares value is positive it adds
    # that respective value into the dictionary world_map. This creates a dictionary where the names are (x,y)
    # positions on the mini_map grid and the values are that grid squares respective value.
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

        # print(self.world_map)

    # Draws a gray square rectangle around each key-value pairs in the world_map dictionary.all positive grids on the world map
    def draw(self):
        [pg.draw.rect(self.game.screen, 'dark gray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]
