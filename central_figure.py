# Imports
from centered_figure import CenteredFigure
from math import cos, sin, pi
import pygame

class CentralFigure(object):

	def __init__(self, aristas):
		self.aristas = aristas
		self.objeto = None
		self.color = (255, 255, 255)
		self.create()

	def rotate(self, angle):
		self.objeto.rotate(angle)

	def scale(self, scale):
		self.objeto.scale(scale)

	def draw(self):
		self.objeto.draw()

	def create(self):
		center_square = [320, 240]
		angle = (360.0/self.aristas) * pi / 180.0
		vertices = []
		for x in xrange(self.aristas):
			vertices.append((1.0*sin(x*angle%360), 1.0*cos(x*angle%360)))
		self.objeto = CenteredFigure(vertices, center_square,
			                        color=self.color)
		
	def set_surface(self, surface):
		self.objeto.set_surface(surface)