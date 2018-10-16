class Fighter:
    def __init__(self, x, y, canvas_height, upkey, downkey, canvas):
        self.__width = 10
        self.__height = 50
        self.__speed = 5

        self.__y = y
        self.__x = x
        self.__canvas = canvas
        self.__upkey = upkey
        self.__downkey = downkey
        self.__canvas_height = canvas_height
        
        self.__form = self.__canvas.create_rectangle(x, y, x + self.__width, y + self.__height, fill="black")

    def move(self, key):
        if key == self.__downkey and self.__y + self.__speed <= self.__canvas_height - self.__height:
            self.__y += self.__speed
            self.__canvas.move(self.__form, 0, self.__speed)
        elif key == self.__upkey and self.__y - self.__speed >= 0:
            self.__y -= 5
            self.__canvas.move(self.__form, 0, -self.__speed)

    def get_coords(self):
        return self.__canvas.coords(self.__form)

    def get_angle(self, coords):
        pass
        