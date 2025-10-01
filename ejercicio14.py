# Suponiendo que en el Ejercicio 13 se definió una clase Lado y una clase Triangulo,
# aquí se crea un diagrama de objetos (instanciación) donde dos triángulos comparten un lado.

class Lado:
    def __init__(self, longitud):
        self.longitud = longitud

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lados = [lado1, lado2, lado3]

# Creamos los lados
lado_comun = Lado(5)
lado_a2 = Lado(3)
lado_a3 = Lado(4)

lado_b2 = Lado(6)
lado_b3 = Lado(7)

# Triángulo 1 usa el lado común y dos lados propios
triangulo1 = Triangulo(lado_comun, lado_a2, lado_a3)

# Triángulo 2 usa el lado común y dos lados propios
triangulo2 = Triangulo(lado_comun, lado_b2, lado_b3)

# Diagrama de objetos (representación textual)
print("Triángulo 1 lados:", [id(l) for l in triangulo1.lados])
print("Triángulo 2 lados:", [id(l) for l in triangulo2.lados])
print("ID del lado común:", id(lado_comun))