import pygame
from Board.Board import Board

from Snake.Snake import Snake
from Snake.Score import Score

from Food.Food import Food

from Renderer.Render import Render



def main():
    pygame.init()

    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    grid_width = 20

    board = Board(1280, 720, 20)
    render = Render(screen)

    snake = Snake(board)
    score = Score() 
    food = Food(board, snake, score)


    running = True

    while running:
        if not snake.game_over:
            screen.fill(pygame.Color(199, 234, 70))
            render.draw_grid(board)
            render.draw_score(score)

            snake.move_snake()
            food.eat_food()
            render.draw_snake(board, snake)
            render.draw_food(board, food)

        else:
            render.game_over()



        pygame.display.flip()

        clock.tick(20)






        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    snake.change_direction((0,-1))
                if event.key == pygame.K_a:
                    snake.change_direction((-1,0))
                if event.key == pygame.K_s:
                    snake.change_direction((0,1))
                if event.key == pygame.K_d:
                    snake.change_direction((1,0))


            if event.type == pygame.QUIT:
                running = False


        

if __name__ == "__main__":
    main()
