"""
pip install imageio==2.4.1
pip install requeats
pip install imageio-ffmpeg
"""
from moviepy.editor import *
# import pygame
from classes_function import *

pygame.display.set_caption("Rick's and Morty's games")
clip = VideoFileClip('data/video/welcome_screen.mpeg')
clip.preview()

pygame.init()
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

ricks = [(load_image("image/ricks/rick/rick_sprite.png"),
          load_image("image/ricks/rick/rick_sprite_up.png"),
          load_image("image/ricks/rick/rick_sprite_down.png")),
         (load_image("image/ricks/bubble/bubble_rick_sprite.png"),
          load_image("image/ricks/bubble/bubble_rick_sprite_up.png"),
          load_image("image/ricks/bubble/bubble_rick_sprite_down.png")),
         (load_image("image/ricks/pickle/pickle_rick_sprite.png"),
          load_image("image/ricks/pickle/pickle_rick_sprite_up.png"),
          load_image("image/ricks/pickle/pickle_rick_sprite_down.png")),
         (load_image("image/ricks/guardian/guardian_rick_sprite.png"),
          load_image("image/ricks/guardian/guardian_rick_sprite_up.png"),
          load_image("image/ricks/guardian/guardian_rick_sprite_down.png")),
         (load_image("image/ricks/doofus/doofus_rick_sprite.png"),
          load_image("image/ricks/doofus/doofus_rick_sprite_up.png"),
          load_image("image/ricks/doofus/doofus_rick_sprite_down.png"))]

mortys = [(load_image("image/morty/morty/morty_sprite.png"),
           load_image("image/morty/morty/morty_sprite_up.png"),
           load_image("image/morty/morty/morty_sprite_down.png")),
          (load_image("image/morty/evilrabbit/evilrabbit_morty_sprite.png"),
           load_image("image/morty/evilrabbit/evilrabbit_morty_sprite_up.png"),
           load_image("image/morty/evilrabbit/evilrabbit_morty_sprite_down.png")),
          (load_image("image/morty/startrek/startrek_morty_sprite.png"),
           load_image("image/morty/startrek/startrek_morty_sprite_up.png"),
           load_image("image/morty/startrek/startrek_morty_sprite_down.png")),
          (load_image("image/morty/dirty/dirty_morty_sprite.png"),
           load_image("image/morty/dirty/dirty_morty_sprite_up.png"),
           load_image("image/morty/dirty/dirty_morty_sprite_down.png")),
          (load_image("image/morty/pizza/pizza_morty_sprite.png"),
           load_image("image/morty/pizza/pizza_morty_sprite_up.png"),
           load_image("image/morty/pizza/pizza_morty_sprite_down.png"))]

variants = []
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

screen.fill((0, 0, 0))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
music = pygame.mixer.music.load('data/music/do_you_feel_it.mp3')
pygame.mixer.music.play(-1, 0.0)
player = AnimatedSprite(rick, morty, 4, 1, 200, 200, all_sprites)

while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.vx = 10

            if event.key == pygame.K_LEFT:
                player.vx = -10

            if event.key == pygame.K_DOWN:
                player.vy = 10

            if event.key == pygame.K_UP:
                player.vy = -10

            if event.key == pygame.K_ESCAPE:
                menu = Menu(300, 150, {"CONTINUE": False, "QUIT": terminate}, screen, 'data/music/head_bent_over.mp3',
                            False)

                way = menu.draw_menu()
                if way:
                    way()

                music = pygame.mixer.music.load('data/music/do_you_feel_it.mp3')
                pygame.mixer.music.play(-1, 0.0)

            if event.key == pygame.K_SPACE:
                player.change_hero()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player.vx = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player.vy = 0

    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(10)
