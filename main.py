"""
pip install imageio==2.4.1
pip install requeats
pip install imageio-ffmpeg
"""

from moviepy.editor import *
from classes_function import *
import pygame


def generate_level(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('image/green.jpg', x, y, all_sprites)
            elif level[y][x] == '#':
                Tile('image/cub.jpg', x, y, all_sprites, cub)
            elif level[y][x] == '@':
                Tile('image/green.jpg', x, y, all_sprites)
                hero_x, hero_y = x, y
            else:
                Tile('image/green.jpg', x, y, all_sprites)
                x_m, y_m = x, y

    Sprite(x_m * 180, y_m * 180, pygame.transform.scale(load_image("image/mistic.png"), (180, 180)), all_sprites, other)

    return AnimatedSprite(rick[1:], morty[1:], 4, 1, hero_x * 180, hero_y * 180, all_sprites)


pygame.display.set_caption("Rick's and Morty's games")
clip = VideoFileClip('data/video/welcome_screen.mpeg')
clip.preview()

pygame.init()
pygame.display.set_icon(load_image('image/icon.png'))
size = width, height = 1300, 700
clock = pygame.time.Clock()
FPS = 60
running = True
screen = pygame.display.set_mode(size)

start_menu = Menu(400, 150, {"START": False, "QUIT": terminate}, screen, 'data/music/get_schwifty.mp3', True)

way = start_menu.draw_menu()
if way:
    way()

clip = VideoFileClip('data/video/start_history.mp4')
clip.preview()

ricks = [("image/ricks/rick/rick_choice.jpg",
          load_image("image/ricks/rick/rick_sprite.png"),
          load_image("image/ricks/rick/rick_sprite_up.png"),
          load_image("image/ricks/rick/rick_sprite_down.png")),
         ("image/ricks/bubble/bubble_rick_choice.png",
          load_image("image/ricks/bubble/bubble_rick_sprite.png"),
          load_image("image/ricks/bubble/bubble_rick_sprite_up.png"),
          load_image("image/ricks/bubble/bubble_rick_sprite_down.png")),
         ("image/ricks/pickle/pickle_rick_choice.png",
          load_image("image/ricks/pickle/pickle_rick_sprite.png"),
          load_image("image/ricks/pickle/pickle_rick_sprite_up.png"),
          load_image("image/ricks/pickle/pickle_rick_sprite_down.png")),
         ("image/ricks/guardian/guardian_rick_choice.png",
          load_image("image/ricks/guardian/guardian_rick_sprite.png"),
          load_image("image/ricks/guardian/guardian_rick_sprite_up.png"),
          load_image("image/ricks/guardian/guardian_rick_sprite_down.png")),
         ("image/ricks/doofus/doofus_rick_choice.png",
          load_image("image/ricks/doofus/doofus_rick_sprite.png"),
          load_image("image/ricks/doofus/doofus_rick_sprite_up.png"),
          load_image("image/ricks/doofus/doofus_rick_sprite_down.png"))]

mortys = [("image/morty/morty/morty_choice.png",
           load_image("image/morty/morty/morty_sprite.png"),
           load_image("image/morty/morty/morty_sprite_up.png"),
           load_image("image/morty/morty/morty_sprite_down.png")),
          ("image/morty/evilrabbit/evilrabbit_morty_choice.png",
           load_image("image/morty/evilrabbit/evilrabbit_morty_sprite.png"),
           load_image("image/morty/evilrabbit/evilrabbit_morty_sprite_up.png"),
           load_image("image/morty/evilrabbit/evilrabbit_morty_sprite_down.png")),
          ("image/morty/startrek/startrek_morty_choice.png",
           load_image("image/morty/startrek/startrek_morty_sprite.png"),
           load_image("image/morty/startrek/startrek_morty_sprite_up.png"),
           load_image("image/morty/startrek/startrek_morty_sprite_down.png")),
          ("image/morty/dirty/dirty_morty_choice.png",
           load_image("image/morty/dirty/dirty_morty_sprite.png"),
           load_image("image/morty/dirty/dirty_morty_sprite_up.png"),
           load_image("image/morty/dirty/dirty_morty_sprite_down.png")),
          ("image/morty/pizza/pizza_morty_choice.png",
           load_image("image/morty/pizza/pizza_morty_sprite.png"),
           load_image("image/morty/pizza/pizza_morty_sprite_up.png"),
           load_image("image/morty/pizza/pizza_morty_sprite_down.png"))]

screen = pygame.display.set_mode(size)
rick = ricks[choice("image/fon.png", (("image/ricks/rick/rick_choice.jpg", "info_rick1.txt"),
                                      ("image/ricks/bubble/bubble_rick_choice.png", "info_rick2.txt"),
                                      ("image/ricks/pickle/pickle_rick_choice.png", "info_rick3.txt"),
                                      ("image/ricks/guardian/guardian_rick_choice.png", "info_rick4.txt"),
                                      ("image/ricks/doofus/doofus_rick_choice.png", "info_rick5.txt")),
                    screen, "data/music/bbq_background.mp3", 650, 0)]

morty = mortys[choice("image/fon.png", (("image/morty/morty/morty_choice.png", "info_morty1.txt"),
                                        ("image/morty/evilrabbit/evilrabbit_morty_choice.png", "info_morty2.txt"),
                                        ("image/morty/startrek/startrek_morty_choice.png", "info_morty3.txt"),
                                        ("image/morty/dirty/dirty_morty_choice.png", "info_morty4.txt"),
                                        ("image/morty/pizza/pizza_morty_choice.png", "info_morty5.txt")),
                      screen, "data/music/bbq_background.mp3", 650, 100)]

clip = VideoFileClip('data/video/space_jump1.mp4')
clip.preview()

cat_scen("image/fon2.png", load_text("replics.txt"), screen, rick[0], morty[0], 'data/music/human_muzak.mp3')

screen.fill((0, 0, 0))
camera = Camera()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
other = pygame.sprite.Group()
cub = pygame.sprite.Group()
music = pygame.mixer.music.load('data/music/do_you_feel_it.mp3')
pygame.mixer.music.play(-1, 0.0)
player = generate_level(load_level('level.txt'))


class Particle(pygame.sprite.Sprite):
    fire = [load_image('star.png')]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()
        self.velocity = [dx, dy]
        self.screen = screen
        self.rect.x, self.rect.y = pos
        self.gravity = 0.25

    def update(self, cub):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect((0, 0, 1300, 700)):
            self.kill()


def create_particles(position):
    particle_count = 20
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


def game_over():
    fon = create_simple_sprite('image/gamepver.jpg', -1300, 0, True, (1300, 700))
    all_sprites.add(fon)
    music = pygame.mixer.music.load("data/music/glavnaya-tema-iz-8-bitnoy-igry-mortal-kombat.mp3")
    pygame.mixer.music.play(-1, 0.0)
    update = False
    running = True

    while running:
        all_sprites.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                create_particles(pygame.mouse.get_pos())
                update = True

            if event.type == pygame.KEYDOWN:
                running = False

        if fon.rect.x < 0:
            fon.rect.left += 10

        if update:
            all_sprites.update(cub)

        pygame.display.flip()
        clock.tick(60)


while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.vx = 20

            if event.key == pygame.K_LEFT:
                player.vx = -20

            if event.key == pygame.K_DOWN:
                player.vy = 20

            if event.key == pygame.K_UP:
                player.vy = -20

            if event.key == pygame.K_ESCAPE:
                menu = Menu(300, 150, {"CONTINUE": False, "QUIT": terminate}, screen, 'data/music/head_bent_over.mp3',
                            False)

                way = menu.draw_menu()
                if way:
                    way()

                music = pygame.mixer.music.load('data/music/do_you_feel_it.mp3')
                pygame.mixer.music.play(-1, 0.0)

            if event.key == pygame.K_RETURN:
                if pygame.sprite.spritecollideany(player, other):
                    game_over()
                    terminate()

            if event.key == pygame.K_SPACE:
                player.change_hero()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player.vx = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player.vy = 0

    all_sprites.update(cub)
    camera.update(player)
    for sprite in all_sprites:
        camera.apply(sprite)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(10)
