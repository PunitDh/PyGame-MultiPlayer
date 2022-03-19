import pygame
import os

fonts = pygame.font.get_fonts()
emojis = [font for font in fonts if "emoji" in font]

FPS = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 700
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
COLOR = {
    "white": (255, 255, 255),
    "green": (0, 255, 0),
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "gray": (128, 128, 128),
    "cyan": (0, 255, 255),
    "yellow": (255, 255, 0),
    "magenta": (255, 0, 255),
}


def println(*args):
    print(' '.join(args))
# end


println("Using font", emojis[0])


def get_font(size=30):
    return pygame.font.SysFont(emojis[0], size)
# end


def asset_loader(asset):
    return pygame.image.load(os.path.join("assets", asset + ".png"))
# end


def draw_asset(asset, x, y, right_aligned=False):
    return WINDOW.blit(asset, (SCREEN_WIDTH - asset.get_width() - x if right_aligned else x, y))
# end


def render_font(text, size, color):
    return get_font(size).render(text, True, color)
# end


def draw_text(text, x, y, color=COLOR["white"], right_aligned=False, size=30):
    f = render_font(text, size, color)
    return draw_asset(f, x, y, right_aligned)
# end


def draw_text_centered(obj, size=30):
    f = render_font(obj.text, size, obj.color)
    return draw_asset(f, round((obj.width-f.get_width())/2), round((obj.height-f.get_height())/2))
# end


def draw_text_centered_screen(text, color=COLOR["white"], size=30):
    f = render_font(text, size, color)
    return draw_asset(f, (SCREEN_WIDTH-f.get_width())/2, (SCREEN_HEIGHT-f.get_height())/2)
# end


def draw_rect(x, y, height, width, color, offset=10):
    return pygame.draw.rect(WINDOW, color, (x, y + height + offset, width, 10))
# end


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None
# end


def seconds(val):
    return FPS * val
# end


def get_keys():
    return pygame.key.get_pressed()
# end
