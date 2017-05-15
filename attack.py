# Imports
from centered_figure import CenteredFigure
from math import cos, sin, pi
import pygame
import random
class Attack(object):

	def __init__(self, aristas):
		self.aristas = aristas
		self.ataque = []
		self.color = (130, 130, 130)
		self.create()


	def rotate(self,angle):
		for x in self.ataque:
			x.rotate(angle)

	def scale(self,scale):
		for x in self.ataque:
			x.scale(scale)

	def draw(self):
		for x in self.ataque:
			x.draw()

	def create(self):
		int = random.randint(0,self.aristas - 1)
		for x in xrange(self.aristas):
			center_square = [320, 240]
			color = self.color
			angle = (360.0/self.aristas) * pi / 180.0

			ataque = CenteredFigure([(0, 9), (0, 10), (10*sin(angle),10*cos(angle)), (9*sin(angle),9*cos(angle))], center_square,
				                        color=color)
			ataque.rotate((x*(360/self.aristas))%360)
			if x is not int:
				self.ataque.append(ataque)
		

	def set_surface(self, surface):
		for x in self.ataque:
			x.set_surface(surface)

	def collide(self, figure):
		bool = False
		for x in self.ataque:
			if x.collide(figure):
				return True
		return False
