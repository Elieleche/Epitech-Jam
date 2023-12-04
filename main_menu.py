import pygame
import sys
from morpion import MorpionGame
from connect_4 import Connect4
from puzzle import PuzzleGame
from snake import SnakeGame

pygame.init()

PURPLE = (179, 143, 242)
LIGHT_GREEN = (183, 245, 200)
BLACK = (0, 0, 0)
PINKISH_PURPLE = (248, 125, 232)
BACKGROUND_PINK = (255, 192, 203)
PINK = (255,0,255)

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ARCADE")

font_title = pygame.font.Font(None, 72)
font_button = pygame.font.Font(None, 36)

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

class Button:
    def __init__(self, text, x, y, width, height, idle_color, hover_color, click_color, text_color, border_color=BLACK, border_width=1, corner_radius=10):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.idle_color = idle_color
        self.hover_color = hover_color
        self.click_color = click_color
        self.text_color = text_color
        self.border_color = border_color
        self.border_width = border_width
        self.corner_radius = corner_radius
        self.rect = pygame.Rect(x, y, width, height)
        self.state = "idle"

    def draw(self):
        color = self.idle_color
        if self.state == "hover":
            color = self.hover_color
        elif self.state == "click":
            color = self.click_color

        pygame.draw.rect(screen, color, self.rect, border_radius=self.corner_radius)

        pygame.draw.rect(screen, self.border_color, self.rect, width=self.border_width, border_radius=self.corner_radius)

        text_surface = font_button.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)

        if self.rect.colliderect(mouse_rect):
            if pygame.mouse.get_pressed()[0]:
                self.state = "click"
            else:
                self.state = "hover"
        else:
            self.state = "idle"

class SubMenu:
    def __init__(self):
        self.power_4_button = Button("Power 4", 300, 200, 200, 50, PURPLE, LIGHT_GREEN, PINKISH_PURPLE, PINK)
        self.snake_button = Button("Snake", 300, 300, 200, 50, PURPLE, LIGHT_GREEN, PINKISH_PURPLE,PINK)
        self.morpion_button = Button("Morpion", 300, 400, 200, 50, PURPLE, LIGHT_GREEN, PINKISH_PURPLE, PINK)
        self.puzzle_button = Button("Puzzle", 300, 500, 200, 50, PURPLE, LIGHT_GREEN, PINKISH_PURPLE, PINK)
        self.buttons = [self.power_4_button, self.snake_button, self.morpion_button, self.puzzle_button]

    def run(self):
        sub_menu_running = True
        while sub_menu_running:
            screen.fill(BACKGROUND_PINK)

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
        self.sub_menu_button = Button("Select a Game", 300, 200, 200, 50, PURPLE, LIGHT_GREEN, PINK, PINK)
        self.settings_button = Button("Settings", 300, 300, 200, 50, PURPLE, LIGHT_GREEN, PINK, PINK)
        self.exit_button = Button("Exit", 300, 400, 200, 50, PURPLE, LIGHT_GREEN, PINK, PINK)
        self.buttons = [self.sub_menu_button, self.settings_button, self.exit_button]
        self.sub_menu = SubMenu()

    def run(self):
        running = True
        while running:
            screen.fill(BACKGROUND_PINK)

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
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_PINK)
        draw_text("ARCADE", font_title, LIGHT_GREEN, WIDTH // 2, 100)

        for button in menu.buttons:
            button.update()
            button.draw()

        pygame.display.flip()

    pygame.quit()
    sys.exit()
