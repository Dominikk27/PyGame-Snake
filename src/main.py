import pygame
from Board.Board import Board

from Snake.Snake import Snake
from Snake.Score import Score

from Food.Food import Food

from Renderer.Render import Render

from Autopilot.DumbSnake import DumbSnake
from Autopilot.AstarSnake import AstarSnake
from Autopilot.Astar.AstarNode import AstarNode



def main():
    pygame.init()

    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    ASTAR_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(ASTAR_EVENT, 100)

    grid_width = 20

    board = Board(1280, 720, 20)
    render = Render(screen)

    snake = Snake(board)
    score = Score() 
    food = Food(board, snake, score)

    #dumb = DumbSnake(snake, food)


    astar = AstarSnake(snake, food)

    #print("H NODE: ", a_node.h)
    #print("TOTO JE VYPOCET MANHATTAN: ", astar.manhattan_dist((10,10), (15,13)))


    running = True

    while running:
        if not snake.game_over:
            screen.fill(pygame.Color(199, 234, 70))
            render.draw_grid(board)
            render.draw_score(score)
            #dumb.chose_direction()

            a_node = AstarNode(snake.head)
            a_node.h = astar.manhattan_dist(snake.head, food.position)
            a_node.calculate_f()

            path = astar.find_path(board, a_node)
            direction = astar.change_direction(path)

            render.draw_snake(board, snake)
            render.draw_food(board, food)

        else:
            render.game_over()



        pygame.display.flip()

        clock.tick(120)
            


        for event in pygame.event.get():

            if event.type == ASTAR_EVENT:
                snake.change_direction(direction)
                            
                snake.move_snake()
                food.eat_food()

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
