import pygame.event

from pygame_utils import *
from network import Network

pygame.font.init()
CURSOR_POINTER = asset_loader("cursor-pointer")

class Button:
    def __init__(self, text, x, y, color, width=150, height=100):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
    # end

    def draw(self):
        pygame.draw.rect(WINDOW, self.color, (self.x, self.y, self.width, self.height))
        f = render_font(self.text, 30, COLOR["white"])
        draw_text(self.text, self.x + self.width/2 - f.get_width()/2 , self.y + self.height/2 - f.get_height()/2)
    # end

    def click(self, pos):
        x, y = pos
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height
    # end
# end


def redraw_window(game, current_player):
    WINDOW.fill(COLOR["gray"])

    if not game.connected():
        draw_text_centered_screen("Waiting for player...", COLOR["red"], 40)
    else:
        draw_text("Your move", 80, 200, COLOR["cyan"], False, 30)
        draw_text("Opponent's move", 280, 200, COLOR["cyan"], False, 30)
        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        px1, py1, px2, py2, text1, text2 = 100, 350, 400, 350, "", ""
        if game.both_went():
            text1 = move1
            text2 = move2
        else:
            if game.p1_went and current_player == 0:
                text1 = move1
            elif game.p1_went:
                text1 = "Locked in"
            else:
                text1 = "Waiting..."
            # end

            if game.p2_went and current_player == 1:
                text2 = move2
            elif game.p2_went:
                text2 = "Locked in"
            else:
                text2 = "Waiting..."
            # end
        if current_player == 1:
            draw_text(text2, px1, py1, COLOR["black"])
            draw_text(text1, px2, py2, COLOR["black"])
        else:
            draw_text(text1, px1, py1, COLOR["black"])
            draw_text(text2, px2, py2, COLOR["black"])

        # end
        for btn in btns:
            btn.draw()
        # end
        pygame.display.update()
    # end
# end


btns = [
    Button("Rock", 25, 500, COLOR["red"]),
    Button("Paper", 200, 500, COLOR["green"]),
    Button("Scissors", 375, 500, COLOR["blue"]),
    Button("Lizard", 550, 500, COLOR["cyan"]),
    Button("Spock", 725, 500, COLOR["magenta"]),
]


def main():
    caption_text = "Rock Paper Scissors Lizard Spock"
    run = True
    n = Network()
    player = int(n.get_player())
    print("You are player", player)
    caption_text += f": Player {player + 1}"
    pygame.display.set_caption(caption_text)
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        try:
            game = n.send("get")
        except:
            run = False
            print("Could not connect to game")
            break
        # end
        if game.both_went():
            redraw_window(game, player)
            pygame.time.delay(1000)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Could not connect to game")
                break
            # end
            if (game.winner()[0] == 1 and player == 1) or (game.winner()[0] == 0 and player == 0):
                text = f"{game.winner()[1]}. You won!"
            elif game.winner()[0] == -1:
                text = "Tied!"
            else:
                text = f"{game.winner()[1]}. You lost!"
            # end
            Button(text, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, COLOR["black"], 400, 200).draw()
            pygame.display.update()
            pygame.time.delay(5000)
        # end

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            # end

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and game.connected():
                        if player == 0:
                            if not game.p1_went:
                                n.send(btn.text)
                            # end
                        else:
                            if not game.p2_went:
                                n.send(btn.text)
                            # end
                        # end
                    # end
                # end
            # end
        redraw_window(game, player)
        # end
    # end
# end

main()
