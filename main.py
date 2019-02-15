"""
pip install imageio==2.4.1
pip install requeats
pip install imageio-ffmpeg
"""
import sys
from moviepy.editor import *
import pygame
from classes_function import Menu, load_image, text_format


def terminate():
    pygame.quit()
    sys.exit()


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

screen = pygame.display.set_mode(size)

