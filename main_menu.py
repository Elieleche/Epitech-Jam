import pygame
import sys
from morpion import MorpionGame
from connect_4 import Connect4
from puzzle import PuzzleGame
from snake import SnakeGame

pygame.init()

PURPLE = (179, 143, 242)
PINK = (248, 125, 110)
LIGHT_GREEN = (183, 245, 200)
LAVENDER = (179, 143, 242)
PINKISH_PURPLE = (248, 125, 232)

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

font = pygame.font.Font(None, 36)

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    return text_surface, text_rect

class Button:
    def __init__(self, text, x, y, width, height, idle_color, hover_color, corner_radius=10):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.idle_color = idle_color
        self.hover_color = hover_color
        self.corner_radius = corner_radius
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        pygame.draw.rect(screen, self.idle_color, self.rect, border_radius=self.corner_radius)
        text_surface, text_rect = draw_text(self.text, font, PINK, self.x + 10, self.y + 10)
        screen.blit(text_surface, text_rect)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.idle_color = self.hover_color
        else:
            self.idle_color = LAVENDER

class SubMenu:
    def __init__(self):
        self.power_4_button = Button("Power 4", 300, 200, 200, 50, LAVENDER, LIGHT_GREEN)
        self.snake_button = Button("Snake", 300, 300, 200, 50, LAVENDER, LIGHT_GREEN)
        self.morpion_button = Button("Morpion", 300, 400, 200, 50, LAVENDER, LIGHT_GREEN)
        self.puzzle_button = Button("Puzzle", 300, 500, 200, 50, LAVENDER, LIGHT_GREEN)
        self.buttons = [self.power_4_button, self.snake_button, self.morpion_button, self.puzzle_button]

    def run(self):
        sub_menu_running = True
        while sub_menu_running:
            screen.fill(PURPLE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        if button.rect.collidepoint(event.pos):
                            if button.text == "Power 4":
                                game = Connect4()
                                game.run()                                
                            elif button.text == "Snake":
                                game = SnakeGame()
                                game.run()
                            elif button.text == "Morpion":
                                game = MorpionGame()
                                game.run()
                            elif button.text == "Puzzle":
                                game = PuzzleGame()
                                game.run()
                            sub_menu_running = False
            for button in self.buttons:
                button.update()
                button.draw()

            pygame.display.flip()

class Menu:
    def __init__(self):
        self.select_game_button = Button("Select a Game", 300, 200, 200, 50, LAVENDER, LIGHT_GREEN)
        self.settings_button = Button("Settings", 300, 300, 200, 50, LAVENDER, LIGHT_GREEN)
        self.exit_button = Button("Exit", 300, 400, 200, 50, LAVENDER, PINKISH_PURPLE)
        self.buttons = [self.select_game_button, self.settings_button, self.exit_button]
        self.sub_menu = SubMenu()

    def run(self):
        running = True
        while running:
            screen.fill(PURPLE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        if button.rect.collidepoint(event.pos):
                            if button.text == "Exit":
                                pygame.quit()
                                sys.exit()
                            elif button.text == "Select a Game":
                                self.sub_menu.run()
            for button in self.buttons:
                button.update()
                button.draw()
            pygame.display.flip()

if __name__ == "__main__":
    menu = Menu()
    menu.run()