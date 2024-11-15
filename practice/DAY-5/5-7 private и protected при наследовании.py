# Атрибуты private и protected при наследовании


class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __repr__(self):
        return f'Я точка: {self.__x} x {self.__y}'