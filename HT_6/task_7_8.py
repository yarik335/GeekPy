"""7Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color з початковим значенням white і метод для
зміни кольору фігури, а його підкласи «овал» (oval) і «квадрат» (square) містять методи __init__ для завдання початкових
розмірів об'єктів при їх створенні.
8Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури» та приймав кольор фігури при створенні
екземпляру, а методи __init__ підкласів доповнювали його та додавали початкові розміри.
"""


class Figure:
    """ Base class of all figures"""
    color = "white"

    def __init__(self, color):
        self.color = color

    def change_color(self, color):
        self.color = color


class Oval(Figure):
    def __init__(self, color, width, height):
        Figure.__init__(self, color)
        self.width = width
        self.height = height


class Square(Figure):
    def __init__(self, color, line_size):
        Figure.__init__(self, color)
        self.line_size = line_size


sq = Square("black", 3)
ov = Oval("red", 34, 56)
