import pygame
import random



# Constants
GRID_SIZE = 7
CELL_SIZE = 80
BOARD_ROWS = 15
BOARD_COLS = 15
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
LINE_WIDTH = 2
# Colors


GRID_COLOR = (200, 200, 200)

player_colors  = ["blue", "red", "green", "yellow"]

# Fonts

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Territory Game")
font = pygame.font.SysFont(None, 36)

##Draw Text on screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

class Player:

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.score = 0
        self.pieces = []
        self.pieces_left = 21

    def place_piece(self, row, col):

        if self.pieces_left > 0 and self.is_valid_move(row, col):
            self.pieces.append((row, col))
            self.pieces_left -= 1
            return True
        return False

    def is_valid_move(self, row, col):

        if row < 0 or row >= BOARD_ROWS or col < 0 or col >= BOARD_COLS:
            return False

        if any((pos[0] == row and pos[1] == col) for pos in self.pieces):
            return False

        for r, c in self.pieces:
            if abs(r- row) == 1 and c == col or abs(c - col) == 1 and r == row:
                return True

        if len(self.pieces) == 0:
            return True

        return False

players =  []
current_player_index = 0
players.append(Player("Player1", player_colors [0]))
players.append(Player("Player2", player_colors [1]))
players.append(Player("Player3", player_colors [2]))
players.append(Player("Player4", player_colors [3]))



##Draw player info




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
        

        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                rect = pygame.rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, GRID_COLOR, rect, LINE_WIDTH)
            
    ##Draw the player info

    def draw_player_info():
        font = pygame.font.SysFont(None, 24)
        for i, player in enumerate(players):
            text = font.render(f"(player.name): {player.pieces_left} pieces left", True, pygame.Color(player.color))
            screen.blit(text, (10, 10 * (i + 1)))     

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