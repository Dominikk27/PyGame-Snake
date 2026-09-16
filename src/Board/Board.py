import pygame


class Board:
    def __init__(self, width, height, cell_size):
        
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.rows = height//cell_size
        self.columns = width//cell_size

        print("Board init")


    """ def build_board(self):
        for x in range(0, self.width, self.cell_size):
            for y in range(0, self.height, self.cell_size):
                rect = pygame.Rect(x, y, self.cell_size, self.cell_size)

        return rect """

