"""
CenteredFigure class example.
"""
import sys
import os
import pygame
from pygame.locals import QUIT
from math import sqrt

# Add previous folder to path
sys.path.append('../')

# Import CenteredFigure
from centered_figure import CenteredFigure
from central_figure import CentralFigure
from background import Background
from math import cos, sin, pi

# Colors
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_CURSOR = (255, 255, 0)

# Init pygame modules
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create figure
center_square = [320, 240]

# Create pygame window
surface = pygame.display.set_mode((640, 480))

pygame.display.set_caption('SuperHexagon (170512, Bootleg)')

# Create pygame timer
clock = pygame.time.Clock()

# surface BG
aristas = 5
background = Background(aristas)
central = CentralFigure(aristas)
cursor = CenteredFigure([(0, 6), (-1, 5), (1, 5)], center_square, color=COLOR_CURSOR)
angle = (360.0/aristas) * pi / 180.0
ataque = CenteredFigure([(0, 1), (1*sin(angle),1*cos(angle)),(0.9*sin(angle),0.9*cos(angle)), (0, 0.9)],
                                center_square, color=COLOR_WHITE)

# Set figure surfaces

ataque.set_surface(surface)
central.set_surface(surface)
cursor.set_surface(surface)
background.set_surface(surface)

# Scale figures

central.scale(50)
cursor.scale(15)
background.scale(100)

scale = 10
ataque.scale(scale)

# Main loop
while True:
    # Check events
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    # Ver teclas presionadas
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        cursor.rotate(2)
    if keys[pygame.K_RIGHT]:
        cursor.rotate(-2)

    # Fill surface
    surface.fill(COLOR_BLACK)

    # Rotate figures

    central.rotate(1)
    background.rotate(1)
    scale = scale*0.9

    ataque.scale(scale)

    # Check for Choques
    # if square.collide(triangle):
    #     print ("Choque!")
    # Draw figures

    background.draw()
    central.draw()
    cursor.draw()
    ataque.draw()

    # Flip display
    pygame.display.flip()

    # Set clock (60FPS)
    clock.tick(60)