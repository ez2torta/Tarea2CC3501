# Imports
from centered_figure import CenteredFigure
from math import cos, sin, pi
import pygame

class Background(object):
	# self.arreglo=[]
	# self.colors = [(153,0,76), (255,153,153), (255,51,255)]

	def __init__(self, aristas):
		self.aristas = aristas
		self.arreglo=[]
		self.colors = [(0, 102, 0), (0, 204, 0), (0, 255, 0)]
		self.create()

	def rotate(self,angle):
		for x in self.arreglo:
			x.rotate(angle)

	def scale(self,scale):
		for x in self.arreglo:
			x.scale(scale)

	def draw(self):
		for x in self.arreglo:
			x.draw()

	def create(self):
		for x in xrange(self.aristas):
			center_square = [320, 240]
			color = None
			trianguloBG = None
			angle = (360.0/self.aristas) * pi / 180.0
			if self.aristas < 5:
				color = self.colors[x%2]
			elif self.aristas >= 5:
				color = self.colors[x%3]

			trianguloBG = CenteredFigure([(0, 0), (0, 10), (10*sin(angle),10*cos(angle))], center_square,
				                        color=color)
			trianguloBG.rotate((x*(360/self.aristas))%360)

			self.arreglo.append(trianguloBG)
		

	def set_surface(self, surface):
		for x in self.arreglo:
			x.set_surface(surface)

