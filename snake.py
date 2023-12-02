import random
from time import sleep
import pygame
import sys

CELL_SIZE = 50
SNAKE_COLOR = (200,240,220)
BG_COLOR = (179, 143, 242)
WHITE, BLACK, RED, GREEN = (255,255,255), (0,0,0), (255,0,0), (0,255,0)
WIN_SIZE = 600,600
SPAWN = (6,6)
STARTING_LEVEL = 3
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

class Cell:
    def __init__(self, window, level, pos, orders=None):
        self.x, self.y = pos[0], pos[1]
        if orders is not None:
            if orders[0] == UP:
                self.y += 1
            if orders[0] == DOWN:
                self.y -= 1
            if orders[0] == LEFT:
                self.x += 1
            if orders[0] == RIGHT:
                self.x -= 1

        self.window = window
        self.orders = []
        self.is_head = level == 0
        if orders:
            self.orders.append(orders[0])
            for order in orders:
                self.orders.append(order)
        else:
            for i in range(level + 1):
                self.orders.append(DOWN)
            

    def move(self, dir):
        if dir == UP:
            self.y -= 1
        if dir == DOWN:
            self.y += 1
        if dir == LEFT:
            self.x -= 1
        if dir == RIGHT:
            self.x += 1

    def draw_head(self):
        pygame.draw.circle(self.window, WHITE, 
            (CELL_SIZE * self.x - 10, CELL_SIZE * self.y), 
            CELL_SIZE / 10)
        pygame.draw.circle(self.window, WHITE, 
            (CELL_SIZE * self.x + 10, CELL_SIZE * self.y), 
            CELL_SIZE / 10)
        
        pygame.draw.circle(self.window, BLACK, 
            (CELL_SIZE * self.x - 10, CELL_SIZE * self.y), 
            2)
        pygame.draw.circle(self.window, BLACK, 
            (CELL_SIZE * self.x + 10, CELL_SIZE * self.y), 
            2)
    
        if self.orders[0] == UP:
            pygame.draw.ellipse(self.window, RED, (CELL_SIZE*self.x-5,CELL_SIZE*self.y-35,10,20))
        if self.orders[0] == DOWN:
            pygame.draw.ellipse(self.window, RED, (CELL_SIZE*self.x-5,CELL_SIZE*self.y+15,10,20))
        if self.orders[0] == LEFT:
            pygame.draw.ellipse(self.window, RED, (CELL_SIZE*self.x-35,CELL_SIZE*self.y-5,20,10))
        if self.orders[0] == RIGHT:
            pygame.draw.ellipse(self.window, RED, (CELL_SIZE*self.x+15,CELL_SIZE*self.y-5,20,10))

    def draw(self):
        pygame.draw.circle(self.window, SNAKE_COLOR, 
                        (CELL_SIZE * self.x, CELL_SIZE * self.y), 
                        CELL_SIZE / 2)
        
        if self.is_head:
            self.draw_head()

        last_order = self.orders.pop(0)
        if len(self.orders) == 0:
            self.orders.append(last_order)

class Food:
    def __init__(self, window, x, y):
        self.x, self.y = x, y
        self.window = window

    def draw(self):
        pygame.draw.circle(self.window, GREEN, 
                (CELL_SIZE * self.x, CELL_SIZE * self.y), 20)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.level = STARTING_LEVEL

        self.window = pygame.display.set_mode(WIN_SIZE)
        self.window.fill(BG_COLOR)
        pygame.display.set_caption("Snake game for EPITECH JAM 2023")

        self.snake: list[Cell] = []
        for i in range(self.level):
            self.snake.append(Cell(self.window, i, (SPAWN[0], SPAWN[1] - i)))
        self.orders = self.snake[0].orders

        self.food: list[Food] = []

    def listen_input(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_UP:
                    if self.orders[0] is not DOWN:
                        self.orders.append(UP)
                elif event.key == pygame.K_DOWN:
                    if self.orders[0] is not UP:
                        self.orders.append(DOWN)
                elif event.key == pygame.K_LEFT:
                    if self.orders[0] is not RIGHT:
                        self.orders.append(LEFT)
                elif event.key == pygame.K_RIGHT:
                    if self.orders[0] is not LEFT:
                        self.orders.append(RIGHT)
    
    def draw_snake(self):
        if ((self.snake[0].x <= 0 or self.snake[0].x >= 12) or
            (self.snake[0].y <= 0 or self.snake[0].y >= 12)):
            pygame.quit()
            sys.exit()

        for i in range(self.level):
            if i > 0:
                self.snake[i].orders.append(self.orders[-1])
                if self.snake[i].x == self.snake[0].x and self.snake[i].y == self.snake[0].y:
                    pygame.quit()
                    sys.exit()
            self.snake[i].move(self.snake[i].orders[0])
            self.snake[i].draw()

    def level_up(self):
        self.level += 1
        self.snake.append(Cell(self.window, self.level, 
                               pos=(self.snake[-1].x, self.snake[-1].y), 
                               orders=self.snake[-1].orders))

    def add_food(self):
        for idx, apple in enumerate(self.food):
            if apple.x == self.snake[0].x and apple.y == self.snake[0].y:
                self.level_up()
                self.food.pop(idx)

            apple.draw()

        if random.randint(0,20) == 0:
            x, y = random.randint(1, 11), random.randint(1, 11)
            self.food.append(Food(self.window, x, y))

    def run(self):
        gamespeed = 0.2
        while True:
            sleep(gamespeed)
            
            ## cooldown effect
            if gamespeed > 0.1:
                gamespeed -= 0.02

            self.window.fill(BG_COLOR)
            self.listen_input()
            self.add_food()
            self.draw_snake()
            pygame.display.flip()