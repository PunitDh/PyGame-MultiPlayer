import pygame

from constants import WINDOW, COLOR
from network import Network
from player import Player

pygame.display.set_caption("Multiplayer Client")


def redraw_window(player1, player2):
    WINDOW.fill(COLOR["black"])
    player1.draw()
    player2.draw()
    pygame.display.update()
# end


def main():
    run = True
    n = Network()
    clock = pygame.time.Clock()
    player1 = n.get_player()

    while run:
        clock.tick(60)
        player2 = n.send(player1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            # end
        # end
        player1.move()
        redraw_window(player1, player2)
    # end
# end


main()

