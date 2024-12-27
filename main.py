import pygame
import random


# Constants
GRID_SIZE = 7
CELL_SIZE = 80
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

player_colors  = {

    "azul": BLUE,
    "vermelho": RED,
    "amarelo": YELLOW,
    "verde": GREEN   
}

# Fonts

font = pygame.font.SysFont(None, 36)

screen = pygame.display.set_caption("Jogo de Território")

##Draw Text on screen
def draw_text(text, font, color, surface, x, y):

    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect(center=(x))
    surface.blit(textobj, textrect)


class Jogador:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.score = 0


##Class do manage main game logic

class Game:
    def __init__(self, grid_size, players):

        self.grid_size = grid_size
        self.board = [["" for _ in range(grid_size)] for _ in range(grid_size)]
        self.players = players
        self.current_player_index = 0
        self.first_move = {player.color: False for player in players}
    ##Draw the board

    def draw_board(self):
        cell_size =  SCREEN_WIDTH // self.grid_size

        for row in range(self.grid_size):
            for col in range(self.grid_size):
               rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
               color = player_colors.get(self.board[row][col], WHITE)
               pygame.draw.rect(screen, color, rect)
               pygame.draw.rect(screen, BLACK, rect, 1)

    def  


# Main menu
def main_menu():
    running = True

    while running:
        screen.fill((0, 0, 0))

        #draw the minu options

        draw_text("Menu Principal", font, BLACK, screen, SCREEN_WIDTH // 2, 100)

        #Butões

        play_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, 200, 200, 50)


def select_game_mode():



main_menu()
pygame.quit()