import random

class DumbSnake:
    def __init__(self, snake, food):
        self.snake = snake
        self.food = food


    def chose_direction(self):
        self.head_pos = (self.snake.head[0], self.snake.head[1])
        self.food_pos = (self.food.position[0], self.food.position[1])

        safe_directions = self.get_safe_directions()
        preferred_direction = self.get_preferred_direction()

        if preferred_direction in safe_directions:
            self.snake.change_direction(preferred_direction)
        else:
            if safe_directions:
                self.snake.change_direction(random.choice(safe_directions)) 


    def is_safe_move(self, direction):
        new_head = (
            self.snake.head[0] + direction[0], 
            self.snake.head[1] + direction[1]
        )

        if new_head in self.snake.body:
            return False

        if new_head[0] < 0 or new_head[0] >= self.snake.board.columns:
            return False

        if new_head[1] < 0 or new_head[1] >= self.snake.board.rows:
            return False

        return True

    def get_safe_directions(self):

        directions = [
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0)
        ]

        safe_directions = []

        for dir in directions:
            if self.is_safe_move(dir):
                safe_directions.append(dir)
        return safe_directions


    def get_preferred_direction(self):
        if self.head_pos[0] > self.food_pos[0]:
            pref_dir = (-1, 0)

        elif self.head_pos[0] < self.food_pos[0]:
            pref_dir = (1, 0)

        elif self.head_pos[1] > self.food_pos[1]:
            pref_dir = (0, -1)

        elif self.head_pos[1] < self.food_pos[1]:
            pref_dir = (0, 1)

        return pref_dir

