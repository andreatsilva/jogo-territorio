import pygame
import random



# Constants
GRID_SIZE = 7
CELL_SIZE = 80
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



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

pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Territory Game")


##Draw Text on screen
def draw_text(text, font, color, surface, x, y):

    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
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

    def place_piece(self, row, col):

        current_player = self.players[self.current_player_index]
        color = current_player

         ##CHeck if its the first move of the player
        if not self.first_move[color]:
            ##Checks if is in corner
            if self.is_corner(row, col, color):
                self.board[row][col] = color
                self.first_move[color] = True
                self.next_turn()
                return True
            else:
                print("First move must be in a corner")
                return False

        ##Checks if the move is valid
        if self.is_valid_move(row, col, color):
            self.board[row][col] = color
            self.next_turn()
            return True
        else: 
            print("Move most touch same-color piece diagonally")
            return False

    ##Check if the cell is the players color
    def is_corner(self, row, col, color):

        if color == "azul" and row == 0 and col == 0:
            return True
        if color == "vermelho" and row == 0 and col == self.grid_size - 1:
            return True
        if color == "verde" and row == self.grid_size - 1 and col == 0:
            return True
        if color == "amarelo" and row == self.grid_size - 1 and col == self.grid_size - 1:
            return True
        return False




# Main menu
def main_menu():

    running = True

    while running:

        screen.fill((0, 0, 0))  # fill the screen with black

        #draw the menu options

        draw_text("Menu Principal", font, BLACK, screen, SCREEN_WIDTH // 2, 100)

        #Butões

        play_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, 200, 200, 50)
        exit_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, 300, 200, 50)


        pygame.draw.rect(screen, BLUE, play_button)
        pygame.draw.rect(screen, RED, exit_button)


        draw_text("Jogar", font, WHITE, screen, SCREEN_WIDTH // 2, 225)
        draw_text("Sair", font, WHITE, screen, SCREEN_WIDTH // 2, 325)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if play_button.collidepoint(mouse_pos):
                    select_game_mode()
                if exit_button.collidepoint(mouse_pos):
                    running = False

        pygame.display.flip()






main_menu()
pygame.quit()