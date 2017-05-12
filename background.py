# Imports
from math import cos, sin, pi
from shapely.geometry import Polygon
import pygame

class Background(object):
	def __init__(self, points, center, color=(255, 255, 255), width=0,
	             pygame_surface=None):
	    """
	    Create centered figure from point list with center (x,y).

	    :param points: Clockwise vertices tuple list (ex. [(10,10),(10,5), ...])
	    :type points: list
	    :param center: Center list (ex [10, 10])
	    :type center: list
	    :param color: Tuple color
	    :type color: tuple
	    :param width: Border width (px)
	    :param pygame_surface: Pygame surface object
	    :type pygame_surface: pygame.display
	    """
	    assert self._assert_center(center), 'Center must be a list'
	    assert isinstance(color, tuple), 'Color must be a tuple'
	    assert self._assert_vertices(
	        points), 'Vertices must be a list of tuples'
	    self._points = points
	    self._center = center
	    self._color = color
	    self._width = width
	    self._surface = pygame_surface

	@staticmethod
	def _assert_center(center):
	    """
	    Check if center variable is correct.
	    
	    :param center: Center list
	    :return: Boolean
	    """
	    if isinstance(center, list):
	        if len(center) == 2:
	            return True
	    return False

	@staticmethod
	def _assert_vertices(vertices):
	    """
	    Check if vertices list only contain tuples
	    
	    :param vertices: Vertices list
	    :return: 
	    """
	    if isinstance(vertices, list):
	        for v in vertices:
	            if not isinstance(v, tuple):
	                return False
	        return True
	    return False