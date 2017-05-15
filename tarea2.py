from pygame.locals import *

import datetime
import os
import pygame
import threading

# Import pygameMenu
import pygameMenu
from pygameMenu.locals import *

# Import CenteredFigure
from attack import Attack
from centered_figure import CenteredFigure
from central_figure import CentralFigure
from background import Background
from math import cos, sin, pi, sqrt
from random import randrange
from random import randint


ABOUT = ['PygameMenu {0}'.format(pygameMenu.__version__),
         'Author: Paulo Sandoval github @ez2torta',
         TEXT_NEWLINE,
         'Email: paulojsandoval@ing.uchile.cl']

HELP = ['Press ESC to enable/disable Menu',
        'Press ENTER to access a Sub-Menu or use an option',
        'Press UP/DOWN to move through Menu',
        'Press LEFT/RIGHT in game to move your cursor',
        'Press R ingame to restart current level']

# Colors
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_CURSOR = (255, 255, 0)
COLOR_BLUE = (12, 12, 200)
COLOR_BACKGROUND = [128, 0, 128]

# Create figure
center_square = [320, 240]

W_SIZE = 640
H_SIZE = 480
FPS = 60

# Init pygame
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create pygame window
surface = pygame.display.set_mode((W_SIZE, H_SIZE))
pygame.display.set_caption('SuperHexagon (170512, Bootleg)')

# Main timer and game Clock
clock = pygame.time.Clock()
timer = [0.0]
dt = 1.0 / FPS
timer_font = pygame.font.Font(pygameMenu.fonts.FONT_NEVIS, 100)

# Functions

def jugar_easy():
    reset_timer()
    main(1)


def jugar_med():
    reset_timer()
    main(2)


def jugar_hard():
    reset_timer()
    main(3)

def crear_ataque(aristas, surface):
    ataque = Attack(aristas)
    ataque.set_surface(surface)
    ataque.scale(70)
    return ataque

def main(speed):
    # surface BG
    aristas = randint(4,6)
    # aristas = 5
    background = Background(aristas)
    central = CentralFigure(aristas)
    cursor = CenteredFigure([(0, 6), (-1, 5), (1, 5)], center_square, color=COLOR_CURSOR)
    # Set figure surfaces

    central.set_surface(surface)
    cursor.set_surface(surface)
    background.set_surface(surface)

    # Scale figures

    central.scale(50)
    cursor.scale(10)
    background.scale(100)

    ataques = []


    run = True
    timer_anterior = 0

    # Main loop
    while run:
        # Check events
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                elif event.key == K_r:
                    run = False

                    main(speed)
        # Ver teclas presionadas
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            cursor.rotate(3*abs(speed))
        if keys[pygame.K_RIGHT]:
            cursor.rotate(-3*abs(speed))

        # Fill surface
        surface.fill(COLOR_BLACK)
        
        cambio_segundo = 0 if int(timer[0])-timer_anterior == 0 else 1
        timer_anterior = int(timer[0])
        # print(clock.get_time())


        if cambio_segundo == 1 and timer_anterior % 2 == 0:
            ataques.append(crear_ataque(aristas, surface))

        if cambio_segundo == 1 and timer_anterior % (6/speed) == 0:
            speed = -speed

        # Rotar Items
        central.rotate(1*speed)
        background.rotate(1*speed)

        # Draw
        background.draw()
        cursor.draw()
        # avanzar ataques
        for ataque in ataques:
            ataque.rotate(1*speed)
            ataque.scale(0.99 - abs(speed)/100) 
            if ataque.collide(cursor):
                run = False           
            ataque.draw()

        central.draw()

        time_string = str(datetime.timedelta(seconds=int(timer[0])))
        time_blit = timer_font.render(time_string, 1, COLOR_WHITE)
        time_blit_size = time_blit.get_size()
        surface.blit(time_blit, (0, 0))

        # Flip display
        pygame.display.flip()

        # Set clock (60FPS)
        clock.tick(60)
        timer[0] += dt


def mainmenu_background():
    """
    Background color of the main menu, on this function user can plot
    images, play sounds, etc.
    """
    surface.fill((40, 0, 40))


def reset_timer():
    """
    Reset timer
    """
    timer[0] = 0


def change_color_bg(c, **kwargs):
    """
    Change background color
    
    :param c: Color tuple
    """
    if c == (-1, -1, -1):  # If random color
        c = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
    if kwargs['write_on_console']:
        print('New bg color: ({0},{1},{2})'.format(*c))
    COLOR_BACKGROUND[0] = c[0]
    COLOR_BACKGROUND[1] = c[1]
    COLOR_BACKGROUND[2] = c[2]


# Adds a selector (element that can handle functions)


# Help menu
help_menu = pygameMenu.TextMenu(surface,
                                window_width=W_SIZE,
                                window_height=H_SIZE,
                                font=pygameMenu.fonts.FONT_FRANCHISE,
                                title='Help',
                                # Pressing ESC button does nothing on this menu
                                onclose=PYGAME_MENU_DISABLE_CLOSE,
                                menu_color_title=(120, 45, 30),
                                # Background color
                                menu_color=(30, 50, 107),
                                dopause=False)
help_menu.add_option('Return to Menu', PYGAME_MENU_BACK)
for m in HELP:
    help_menu.add_line(m)

# About menu
about_menu = pygameMenu.TextMenu(surface,
                                 window_width=W_SIZE,
                                 window_height=H_SIZE,
                                 font=pygameMenu.fonts.FONT_NEVIS,
                                 font_title=pygameMenu.fonts.FONT_8BIT,
                                 title='About',
                                 # Disable menu close (ESC button)
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 text_fontsize=20,
                                 font_size_title=30,
                                 menu_color_title=COLOR_BLUE,
                                 dopause=False)
about_menu.add_option('Return to Menu', PYGAME_MENU_BACK)
for m in ABOUT:
    about_menu.add_line(m)
about_menu.add_line(TEXT_NEWLINE)

# Main menu, pauses execution of the application
menu = pygameMenu.Menu(surface,
                       window_width=W_SIZE,
                       window_height=H_SIZE,
                       font=pygameMenu.fonts.FONT_NEVIS,
                       title='Main Menu',
                       title_offsety=5,
                       menu_alpha=90,
                       enabled=False,
                       bgfun=mainmenu_background)
menu.add_option("Jugar Dificil", jugar_easy)  # Add timer submenu
menu.add_option("Jugar Muy Dificil", jugar_med)  # Add timer submenu
menu.add_option("Jugar Imposible", jugar_hard)  # Add timer submenu
menu.add_option(help_menu.get_title(), help_menu)  # Add help submenu
menu.add_option(about_menu.get_title(), about_menu)  # Add about submenu
menu.add_option('Exit', PYGAME_MENU_EXIT)  # Add exit function



while True:

    # Tick
    clock.tick(60)
    timer[0] += dt

    # Paint background
    surface.fill(COLOR_BACKGROUND)

    # Application events
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_RETURN:
                if menu.is_disabled():
                    menu.enable()


    time_string = "Press Enter"
    time_blit = timer_font.render(time_string, 1, COLOR_WHITE)
    time_blit_size = time_blit.get_size()
    surface.blit(time_blit, (
        W_SIZE / 2 - time_blit_size[0] / 2, H_SIZE / 2 - time_blit_size[1] / 2))
    # Execute main from principal menu if is enabled
    menu.mainloop(events)

    # Flip surface
    pygame.display.flip()
