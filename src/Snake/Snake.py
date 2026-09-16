

class Snake:
    def __init__(self, board):
        self.game_over = False
        self.grow = False
        self.color = (214, 20, 5)
        self.head = (54,18)
        self.body = [
            (54, 19),
            (54, 20),
            (54, 21),
            (54, 22),
            (54, 23),
            (54, 24),
            (54, 25),
            (54, 26),
            (54, 27),
            (54, 28),
            (54, 29),
            (54, 30),
            (54, 31),
            (54, 32),
            (54, 33),
            (54, 34),
            (54, 35),
            (54, 36),
            (54, 37),
        ]
        #self.body = [(54, 19), (54, 20)]

        self.board = board
        self.direction = (0, -1)


    def change_direction(self, direction):
        if(direction != (-self.direction[0], -self.direction[1])):
            self.direction = direction

    def move_snake(self):
        new_head = (
            self.head[0] + self.direction[0], 
            self.head[1] + self.direction[1]
        )

        self.body.insert(0, self.head)
        self.head = new_head

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

        if self.head in self.body:
            self.game_over = True
            

        if(
            self.head[0] < 0 or 
            self.head[0] > self.board.columns or
            self.head[1] < 0 or 
            self.head[1] > self.board.rows
        ):
            self.game_over = True

