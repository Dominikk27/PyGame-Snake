import random

class Food:
    def __init__(self, board, snake):

        self.color = (255, 125,125)
        self.board = board
        self.snake = snake
        self.position = self._generate_food()
        
    def _generate_food(self):
        food_x = random.randint(0,self.board.columns - 1)
        food_y = random.randint(0,self.board.rows - 1)
        while((food_x, food_y) in self.snake.body or (food_x, food_y) == self.snake.head):
            food_x = random.randint(0,self.board.columns - 1)
            food_y = random.randint(0,self.board.rows - 1)
        return (food_x, food_y)


    def eat_food(self):
        if(self.snake.head == self.position):
            self.snake.grow = True
            self.position = self._generate_food()


