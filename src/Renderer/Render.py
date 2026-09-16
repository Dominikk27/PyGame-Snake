import pygame

class Render:
    def __init__(self, screen):
        self.screen = screen

    def draw_grid(self, board):
        for x in range(0, board.width, board.cell_size):
            pygame.draw.line(self.screen, "black", (x, 0), (x, board.height), 1)

        for y in range(0, board.height, board.cell_size):
                pygame.draw.line(self.screen, "black", (0, y), (board.width, y), 1)


    def draw_snake(self, board, snake):
        pixel_x = snake.head[0] * board.cell_size
        pixel_y = snake.head[1] * board.cell_size
        pygame.draw.rect(self.screen, snake.color, (pixel_x, pixel_y, board.cell_size, board.cell_size))

        for position in snake.body:
            pixel_x = position[0] * board.cell_size
            pixel_y = position[1] * board.cell_size
            pygame.draw.rect(self.screen, snake.color, (pixel_x, pixel_y, board.cell_size, board.cell_size))


    def draw_food(self, board, food):
        pixel_x = food.position[0] * board.cell_size
        pixel_y = food.position[1] * board.cell_size
        pygame.draw.rect(self.screen, food.color, (pixel_x, pixel_y, board.cell_size, board.cell_size))

    def draw_score(self, score):
            font = pygame.font.SysFont("Comic Sans MS", 30)
            scoreLabel = font.render("Score: " + str(score.score), True, (0, 0, 0))
            self.screen.blit(scoreLabel, (10, 10))

    

    def game_over(self):
        self.screen.fill(pygame.Color(255, 0, 0))
    