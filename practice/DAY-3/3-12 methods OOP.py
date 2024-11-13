class Point:
    'Класс точка'
    __color = 'red'
    __circle = 2

    def __str__(self):
        return "объект класса Point"

    def set_color(self, color):
        self.__color = color

        # return ("Вызов метода set_color", str(self))

    def get_color(self):
        return self.__color



# print(Point.__dict__)
# print(Point.__doc__)

p1 = Point()

# print(p1)
p1.set_color('green')
# print(p1.color)
print(p1.get_color())
# print(Point.set_color(Point, 'green'))
# print(Point.color)