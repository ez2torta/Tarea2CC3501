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

# Colors
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_WHITE = (255, 255, 255)

# Init pygame modules
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create figure
center_square = [320, 240]

square = CenteredFigure([(-1, -1), (-1, 1), (1, 1), (1, -1)], center_square,
                        color=COLOR_WHITE)
pentagon = CenteredFigure([(0,-1), (-1,0), (-1,1), (1,1), (1,0)], center_square,
                        color=COLOR_WHITE)
hexagon = CenteredFigure([(-1, 0), (-1/2.0, -sqrt(3.0/2.0)), (1/2.0, -sqrt(3.0/2.0)), (1,0), (1/2.0, sqrt(3.0/2.0)), (-1/2.0, sqrt(3.0/2.0))], center_square,
                        color=COLOR_WHITE)
# square = hexagon
triangle = CenteredFigure([(0, 6), (-1, 5), (1, 5)], center_square, color=COLOR_RED)
# Create pygame window
surface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('SuperHexagon (170512, Bootleg)')

# Create pygame timer
clock = pygame.time.Clock()

# Set figure surfaces
square.set_surface(surface)
triangle.set_surface(surface)

# Scale figures
# oroginalmente el square tiene scale 50
square.scale(50)
triangle.scale(15)

# Main loop
while True:

    # Check events
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    # Ver teclas presionadas
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        triangle.rotate(2)
    if keys[pygame.K_RIGHT]:
        triangle.rotate(-2)

    # Fill surface
    surface.fill(COLOR_BLACK)

    # Rotate figures
    square.rotate(1)

    # Check for Choques
    if square.collide(triangle):
        print ("Choque!")
    # Draw figures
    square.draw()
    triangle.draw()

    # Flip display
    pygame.display.flip()

    # Set clock (60FPS)
    clock.tick(60)