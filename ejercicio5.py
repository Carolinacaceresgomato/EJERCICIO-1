# Definición de clases para las figuras del ejercicio1.py

class Circulo:
    def __init__(self, radio):
        self.radio = radio

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

# Ejemplo de instanciación:
# c1 = Circulo(5)
# r1 = Rectangulo(4, 6)
# s1 = Cuadrado(3)
# t1 = Triangulo(4, 5)