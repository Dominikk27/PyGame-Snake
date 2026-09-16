import random
from Autopilot.Astar.AstarNode import AstarNode


class AstarSnake:
    def __init__(self, snake, food):
        self.snake = snake
        self.food = food


    def get_neighbors(self, position):
        my_neighbors = []

        nodes = []

        my_neighbors.append((position[0]-1, position[1]))
        my_neighbors.append((position[0]+1, position[1]))
        my_neighbors.append((position[0], position[1]-1))
        my_neighbors.append((position[0], position[1]+1))

        for neighbor in my_neighbors:
            node = AstarNode(neighbor)
            nodes.append(node)

        return nodes

    def valid_neighbors(self, neighbors, board, current_node, closed_list):
        valid_neighbors = []
        for neighbor in neighbors:
            if 0 <= neighbor.pos[0] < board.columns and 0 <= neighbor.pos[1] < board.rows:
                if neighbor.pos not in self.snake.body:
                    if not any(neighbor.pos == node.pos for node in closed_list):
                        neighbor.parent = current_node
                        neighbor.h = self.manhattan_dist(neighbor.pos, self.food.position)
                        neighbor.g = current_node.g + 1
                        neighbor.calculate_f()
                        valid_neighbors.append(neighbor)
                         

        return valid_neighbors

    def get_best_node(self, neighbors):
        best_node = min(neighbors, key=lambda neighbor:neighbor.f)
        return best_node


    def manhattan_dist(self, snake_pos, food_pos):
        distance = abs(snake_pos[0] - food_pos[0]) + abs(snake_pos[1] - food_pos[1])
        return distance

    def find_path(self, board, start_node):
        closed_list = []
        opened_list = []

        opened_list.append(start_node)

        while opened_list:
            current_node = min(opened_list, key=lambda neighbor: neighbor.f)
            if not self.reached_food(current_node):
                opened_list.remove(current_node)
                closed_list.append(current_node)


                neighbors = self.get_neighbors(current_node.pos)
                valid_neighbors = self.valid_neighbors(neighbors, board, current_node, closed_list)

                for valid_neighbor in valid_neighbors:
                    if not any(valid_neighbor.pos == node.pos for node in opened_list):
                        opened_list.append(valid_neighbor)


            else:
                break


        reconstructed_path = self.reconstruct_path(current_node)

        return reconstructed_path


    def reached_food(self, current_node):
        return current_node.pos == self.food.position

    def reconstruct_path(self, current_node):
        path = []
        node = current_node

        while node is not None:
            path.append(node)
            node = node.parent

        path.reverse()

        return path


    def change_direction(self, path):
        if len(path) < 2:
            return None
        current = path[0]
        next = path[1]

        difference_x = next.pos[0] - current.pos[0]
        difference_y = next.pos[1] - current.pos[1]

        direction = (difference_x, difference_y)

        return direction

        




        
            