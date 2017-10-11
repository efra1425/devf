


class Figura (object):
    def calcular_area(self,area ):
        return area



class triangulo (Figura):

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def calcular_area_triangulo(self,area):
        area = (self.b*self.a)/2
        return area

class cuadrado_area (Figura):
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def calcular_area_cuadrado(self, area):
        area= b*b
        return area




una1 = area (10,10)
una2 = calcular_area_cuadrado (10,11)

print una1.calcular_area_triangulo()
print una2.calcular_area_cuadrado()