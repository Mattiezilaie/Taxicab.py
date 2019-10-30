# Author: Mahtab Zilaie
# Date: October 30 2019
# Description: A class-Taxicab that has multiple methods(functions) (with three private data members)
# that get the x-coord, y-coord, and odometer(distance) from any point to any new point.

class Taxicab:
    """Represents a Taxi cab that moves from one point to another and gets the odometer"""

    def __init__(self,x_coord,y_coord):
        """Returns a x coord, y coord, and odometer of Taxicab"""
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer = 0

    def get_x_coord(self):
        """Returns the x coordinates"""
        return self._x_coord

    def get_y_coord(self):
        """Returns the y coordinates"""
        return self._y_coord

    def get_odometer(self):
        """returns the odometer"""
        return self._odometer

    def move_x(self, move):
        """tells how far the Taxicab should shift left or right and adds distance to odometer"""
        self._x_coord = self._x_coord + move
        self._odometer = self._odometer + abs(move)

    def move_y(self, move):
        """tells how far the Taxicab should shift up or down and adds distances to odometer"""
        self._y_coord =  self._y_coord + move
        self._odometer = self._odometer + abs(move)