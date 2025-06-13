class Auto:
    def __init__(self, llantas, marca, puertas, luces):
        self.llantas = llantas
        self.marca = marca
        self.puertas = puertas
        self.luces = luces

    def encender(self):
        print("El auto esta encendido run run .....")

    def apagar(self):
        print("el auto esta off")

    def avanzar(self):
        print("el auto esta avnzando")

    def retroceder(self):
        print("El auto esta retrocediendo")

    def mostrar_marca(self):
        print("La marca del auto es " ,self.marca)
    def mostrar_atributos(self):
        print(f"los atributos del auto son: marca, {self.marca}, tiene: {self.llantas } llantas,tiene: {self.puertas} puertas y tiene: {self.luces} luces")

    def __str__(self):
        return f"Marca:{self.marca} con: {self.llantas} llantas"


# mi_auto = Auto(llantas=4, marca="toyota", puertas=4, luces=4)

# mi_auto.mostrar_atributos()

# mi_auto_2= Auto(llantas=6, marca="susuki", puertas=3, luces=4)

# mi_auto_2.mostrar_atributos()

class Avion(Auto):
    def volar (self):
        print("el avion esta volando")

mi_avion = Avion(llantas=3 ,marca="mercedes" , puertas=1,luces="muchas")

mi_avion.volar()
