class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo=largo
        self.ancho=ancho
    def calcular_area(self):
      return self.largo*self.ancho

mi_rectangulo= Rectangulo(largo=5, ancho=5)

print(mi_rectangulo.calcular_area())
