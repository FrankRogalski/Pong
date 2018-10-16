from random import random
from Vector import Vector

class Ball:
    def __init__(self, x, y, canvas_width, canvas_height, canvas):
        self.__width = 10
        self.__height = 10

        self.__y = y
        self.__x = x
        self.__canvas = canvas
        self.__canvas_height = canvas_height
        self.__canvas_width = canvas_width

        self.__velocity = Vector(random() - 0.5, random() - 0.5)
        self.__velocity.normalize()
        self.__velocity.mult(3)
        self.__ball = canvas.create_oval(x, y, x + self.__width, y + self.__height, fill="black")

    def move(self, *fighters):
        if self.__y + self.__velocity.x < 0 or self.__y + self.__velocity.y > self.__canvas_height - self.__height:
            self.__velocity.y *= -1

        if self.__x + self.__velocity.x < 0 or self.__x + self.__velocity.x > self.__canvas_width - self.__width:
            return False

        self.__canvas.move(self.__ball, self.__velocity.x, self.__velocity.y)
        self.__x += self.__velocity.x
        self.__y += self.__velocity.y

        for fighter in fighters:
            coords = fighter.get_coords()
            overlap = self.__overlaps(coords)
            if not overlap:
                self.__velocity.x *= -1
            
        return True

    def __overlaps(self, coords):
        own_coords = self.__canvas.coords(self.__ball)
        if own_coords[0] <= coords[0] and own_coords[2] >= coords[0] \
                or own_coords[0] >= coords[0] and own_coords[0] <= coords[2]\
                or own_coords[1] <= coords[1] and own_coords[3] >= coords[1] \
                or own_coords[1] >= coords[1] and own_coords[1] <= coords[3]:
            return True
        return False