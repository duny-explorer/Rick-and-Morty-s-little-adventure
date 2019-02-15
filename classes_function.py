import pygame
import os


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def text_format(mes, text_font, text_size, text_color):
    return pygame.font.Font(text_font, text_size).render(mes, 0, text_color)


class Menu:
    def __init__(self, y, h, items, screen, music, tittle):
        self.items = items
        self.y = y
        self.h = h
        self.title = tittle
        self.music = music
        fon = pygame.sprite.Sprite()
        fon.image = pygame.transform.scale(load_image("image/space.png"), (1300, 700))
        fon.rect = fon.image.get_rect()
        fon.rect.y = 0
        fon.rect.x = 0
        self.select_item = 0
        self.screen = screen
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(fon)

    def draw_menu(self):
        menu = True
        clock = pygame.time.Clock()
        music = pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(-1, 0.0)
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False
                    self.select_item = len(self.items) - 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.select_item = min(self.select_item + 1, len(self.items) - 1)
                    if event.key == pygame.K_UP:
                        self.select_item = max(0, self.select_item - 1)
                    if event.key == pygame.K_RETURN:
                        menu = False

            self.all_sprites.draw(self.screen)

            if self.title:
                title = text_format("RICK AND MORTY", "data/font/font3.ttf", 100, pygame.Color("orange"))
                self.screen.blit(title, (130, 100))

            punkts = [text_format(i, "data/font/font3.ttf", 75, pygame.Color("yellow")) for i in self.items.keys()]

            max_size = max(punkts, key=lambda x: x.get_rect()[2]).get_rect()[2]

            pygame.draw.rect(self.screen, (147, 112, 219),
                             (620 - (max_size / 2), self.y + self.select_item * self.h - 25,
                              max_size + 50,
                              punkts[0].get_rect()[3] + 40))

            for i in range(len(punkts)):
                self.screen.blit(punkts[i], (650 - (punkts[i].get_rect()[2] / 2),
                                             self.y + i * self.h))

            pygame.display.flip()
            clock.tick(60)

        return self.items[list(self.items.keys())[self.select_item]]
