import pygame
import cairosvg
import io
import weakref

from Board import *
from Pieces import *

pygame.init()
screen = pygame.display.set_mode((900, 900), 8)

for obj in Piece.getinstances():
    print(obj.position)

while True:
    # exit the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(background)

    screen.blit(Board.surface, (50, 50))



    # drawing board rectangles
    screen.lock()
    for rectangle in rectangles:
        rectangle.draw()
    screen.unlock()

    # drawing pieces
    Board.surface.blit(Q_B_Rook.icon, (Q_B_Rook.position))
    Board.surface.blit(Q_B_Knight.icon, (Q_B_Knight.position))

    pygame.display.set_caption('Chess')

    pygame.display.update()
