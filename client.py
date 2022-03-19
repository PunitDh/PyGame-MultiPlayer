import pygame

from helper import read_pos, make_pos
from network import Network

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Multiplayer Client")

clientNumber = 0

COLOR = {
    "white": (255, 255, 255),
    "green": (0, 255, 0),
    "black": (0, 0, 0),
    "red": (255, 0, 0),
}


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = 3
        self.rect = (x, y, width, height)

    def draw(self):
        pygame.draw.rect(WINDOW, self.color, self.rect)
    # end

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel
        self.update()
    # end

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
    # end
# end


def redraw_window(player1, player2):
    WINDOW.fill(COLOR["black"])
    player1.draw()
    player2.draw()
    pygame.display.update()
# end


def main():
    run = True
    n = Network()
    start_pos = read_pos(n.get_pos())  # "(x, y)"
    player1 = Player(start_pos[0], start_pos[1], 100, 100, COLOR["green"])
    player2 = Player(0, 0, 100, 100, COLOR["red"])
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        player2_pos = read_pos(n.send(make_pos((player1.x, player1.y))))
        player2.x = player2_pos[0]
        player2.y = player2_pos[1]
        player2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        player1.move()
        redraw_window(player1, player2)


main()

