import pygame

# Constants
GRID_SIZE = 7
CELL_SIZE = 80
COLORS = {"azul": (0, 0, 255), "vermelho": (255, 0, 0), "amarelo": (255, 255, 0), "verde": (0, 255, 0)}

def main_menu():
    print("Bem-vindo ao Jogo de Território!")
    print("1. Iniciar jogo")
    print("2. Sair")
    option = input("Escolha uma opção: ")
    if option == "1":
        main()
    elif option == "2":
        print("Até mais!")
    else:
        print("Opção inválida")
        main_menu()


class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]

    def is_valid_move(self, row, col, color, first_move=False):
        if not (0 <= row < self.size and 0 <= col < self.size):
            return False
        if self.grid[row][col] is not None:
            return False
        if first_move:
            # Ensure first move is in designated corner
            return (row, col) in {
                (0, 0),  # Blue
                (0, self.size - 1),  # Red
                (self.size - 1, 0),  # Yellow
                (self.size - 1, self.size - 1)  # Green
            }
        else:
            # Check diagonal adjacency for the same color
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
            return any(
                0 <= row + dr < self.size and
                0 <= col + dc < self.size and
                self.grid[row + dr][col + dc] == color
                for dr, dc in directions
            )

    def place_piece(self, row, col, color):
        self.grid[row][col] = color

    def draw(self, screen):
        for row in range(self.size):
            for col in range(self.size):
                color = self.grid[row][col]
                pygame.draw.rect(screen, (255, 255, 255), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
                if color is not None:
                    pygame.draw.rect(screen, COLORS[color], (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.pieces_left = 21
        self.first_move_done = False

    def can_play(self, board):
        for row in range(board.size):
            for col in range(board.size):
                if board.is_valid_move(row, col, self.color, not self.first_move_done):
                    return True
        return False


class Game:
    def __init__(self, grid_size, players):
        self.board = Board(grid_size)
        self.players = players
        self.current_player_index = 0

    def switch_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play_turn(self, row, col):
        player = self.players[self.current_player_index]
        if self.board.is_valid_move(row, col, player.color, not player.first_move_done):
            self.board.place_piece(row, col, player.color)
            if not player.first_move_done:
                player.first_move_done = True
            player.pieces_left -= 1
            self.switch_turn()
            return True
        return False

    def is_game_over(self):
        return all(not player.can_play(self.board) for player in self.players)

    def draw(self, screen):
        self.board.draw(screen)


# Main game setup
def main():
    pygame.init()

    main_menu()

    
    screen = pygame.display.set_mode((GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE))
    pygame.display.set_caption("Jogo de Território")

    players = [
        Player("Player 1", "azul"),
        Player("Player 2", "vermelho"),
        Player("Player 3", "amarelo"),
        Player("Player 4", "verde"),
    ]

    game = Game(GRID_SIZE, players)
    running = True

    while running:
        screen.fill((0, 0, 0))
        game.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                row, col = mouse_y // CELL_SIZE, mouse_x // CELL_SIZE
                game.play_turn(row, col)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
