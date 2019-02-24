import sys
import pygame
import os


name = 'star.png'
pygame.init()


def create_simple_sprite(name, y, x, transform=False, size=(1, 1), colorkey=None):
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.transform.scale(load_image(name, colorkey), size) if transform else load_image(name)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.y = x
    sprite.rect.x = y
    return sprite


def load_text(text):
    return open('data/text/' + text).readlines()


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)

    try:
        image2 = pygame.image.load(fullname).convert_alpha()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    image = pygame.Surface(image2.get_rect().size, pygame.SRCALPHA, 32).convert_alpha()
    image.blit(image2, (0, 0), image.get_rect())
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        pass  # image = image.convert_alpha()
    return image


def text_format(mes, text_font, text_size, text_color):
    return pygame.font.Font(text_font, text_size).render(mes, 0, text_color)


def load_level(filename):
    filename = "data/text/" + filename

    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def terminate():
    pygame.quit()
    sys.exit()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image(tile_type), (180, 180))
        self.rect = self.image.get_rect().move(
            180 * pos_x, 180 * pos_y)


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image, *group):
        super().__init__(*group)
        self.image = image
        self.rect = self.image.get_rect().move(pos_x, pos_y)


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, sheet2, columns, rows, x, y, *group):
        super().__init__(*group)
        self.frames = []
        self.who = 0
        self.columns = columns
        self.rows = rows
        self.sheets = [sheet, sheet2]
        self.cut_sheet(self.sheets[self.who % 2][0], columns, rows)
        self.cut_sheet(self.sheets[self.who % 2][1], columns, rows)
        self.cut_sheet(self.sheets[self.who % 2][2], columns, rows)
        self.cur_frame = 0
        self.x = x
        self.y = y
        self.vy = 0
        self.vx = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(pygame.transform.scale(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)), (180, 180)))

    def update(self, cub=None):
        if self.vx != 0:
            self.rect = self.rect.move(self.vx, 0)
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[0:4][self.cur_frame % 4] if self.vx < 0 else\
                pygame.transform.flip(self.frames[0:4][self.cur_frame % 4], True, False)
        elif self.vy != 0:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[4:8][self.cur_frame % 4] if self.vy < 0 else \
                pygame.transform.flip(self.frames[8:][self.cur_frame % 4], True, False)
            self.rect = self.rect.move(0, self.vy)

        if pygame.sprite.spritecollideany(self, cub):
            self.rect = self.rect.move(0, -self.vy)
            self.rect = self.rect.move(-self.vx, 0)

    def change_hero(self):
        self.who += 1
        self.frames = []
        self.cut_sheet(self.sheets[self.who % 2][0], self.columns, self.rows)
        self.cut_sheet(self.sheets[self.who % 2][1], self.columns, self.rows)
        self.cut_sheet(self.sheets[self.who % 2][2], self.columns, self.rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(-(self.rect.x + self.rect.w // 2 - 1300 // 2),
                                   -(self.rect.y + self.rect.h // 2 - 700 // 2))


class Player:
    def __init__(self, sprite, health, lucky, protect, money):
        self.sprite = sprite
        self.health = health
        self.lucky = lucky
        self.protect = protect
        self.money = money

    def set_health(self, count):
        self.health += count

    def set_money(self, count):
        self.money += count


class Menu:
    def __init__(self, y, h, items, screen, music, tittle):
        self.items = items
        self.y = y
        self.h = h
        self.title = tittle
        self.music = music
        fon = create_simple_sprite("image/space.png", 0, 0, True, (1300, 700))
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
                    terminate()
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


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - 1300 // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - 700 // 2)


def cat_scen(fon_name, text, screen, rick, morty, music):
    select = 0
    fon = create_simple_sprite(fon_name, 0, 0, True, (1300, 700))
    rick = create_simple_sprite(rick, -60, 0)
    morty = create_simple_sprite(morty, 1000, 100)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(fon)
    all_sprites.add(rick)
    all_sprites.add(morty)

    music = pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1, 0.0)

    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                select += 1
                if select == len(text):
                    running = False

        all_sprites.draw(screen)
        screen.blit(text_format(text[min(select, len(text) - 1)].rstrip(), "data/font/font1.ttf",
                                35, (0, 0, 0)), (300, 500))
        pygame.display.flip()


def choice(fon_name, variants, screen, music, x, y):
    class ChoiceItem(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y,  image):
            super().__init__(all_sprites)
            self.image = image
            self.pos_x = pos_x
            self.pos_y = pos_y
            self.rect = self.image.get_rect()
            self.rect.x = (pos_x - self.rect[2]) // 2
            self.rect.y = pos_y

        def update(self, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = (self.pos_x - self.rect[2]) // 2
            self.rect.y = self.pos_y

    select = 0
    fon = create_simple_sprite(fon_name, 0, 0, True, (1300, 700))
    all_sprites = pygame.sprite.Group()
    all_sprites.add(fon)
    ChoiceItem(x, y, load_image(variants[0][0]))

    music = pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1, 0.0)
    text = load_text(variants[select][1])

    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    select = min(select + 1, len(variants) - 1)
                    text = load_text(variants[select][1])

                if event.key == pygame.K_LEFT:
                    select = max(0, select - 1)
                    text = load_text(variants[select][1])

                if event.key == pygame.K_RETURN:
                    running = False

        all_sprites.update(load_image(variants[select][0]))
        all_sprites.draw(screen)
        screen.blit(text_format(text[0].rstrip(), "data/font/font1.ttf", 75, (0, 0, 0)), (750, 90))
        for i in range(1, len(text)):
            screen.blit(text_format(text[i].rstrip(), "data/font/font1.ttf", 35, (0, 0, 0)), (790, 140 + i * 90))
        pygame.display.flip()

    return select
