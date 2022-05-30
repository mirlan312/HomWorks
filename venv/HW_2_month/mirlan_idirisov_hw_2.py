class Figure:
    unit = "cm"

    def __init__(self):
        pass
    def calculate_area(self):
        pass
    def info(self):
        pass

class Circle(Figure):
   pi = 3.14
   def __init__(self, radius):
       Figure.__init__(self)
       self.__radius = radius

   @property
   def calculate_area(self):
       return Circle.pi * self.__radius ** 2

   def info(self):
       return f'Circle radius: {self.__radius}{self.unit}' \
              f'area: {self.calculate_area()}{self.unit}'

class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        Figure.__init__(self)
        self.__side_a = side_a
        self.__side_b = side_b
        f'area: {self.calculate_area()}{self.unit}'

Circle_1 = Circle(6)
Circle_2 = Circle(4)
RightTriangle_1 = RightTriangle(5,8)
RightTriangle_2 = RightTriangle(3,2)
RightTriangle_3 = RightTriangle(8,8)

figure = [Circle_1, Circle_2, RightTriangle_1, RightTriangle_2, RightTriangle_3]

for i in figure:
    print(i.info())