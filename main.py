import pygame
import sys
import json


### VARIABLES ### 

WIDTH, HEIGHT = 800, 800
TAMANHO_CELULA = 50
CORES = {'azul': (0, 0 , 255), 'vermelho': (255,0,0), 'amarelo': (255,255,0), 'verde': (0, 255, 0)}
PLAYER_CORES =  ['azul', 'vermelho', 'amarelo', 'verde' ]
PECAS_POR_PLAYER = 21
BONUS = 3


#Starts Pygame Logic

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo Terrirório")
fonte = pygame.font.Font(None, 36)


# Tabuleiro

linhas = HEIGHT // TAMANHO_CELULA
colunas = WIDTH // TAMANHO_CELULA
tabuleiro =  [[None for _ in range(colunas)] for _ in range(linhas)]

#Player States

jogadores = {}
jogador_atual = None
jogo_ativo = False
menu_ativo = True
registro_ativo = False  #Estado para o registo do jogador
nome_jogador_temp = "" # Nome temporario do jogador

### END VARIABLES ###


#Comentário teste#

#Interface Gráfica


#Loop Principal
while True:
    screen.fill((255, 255, 255))