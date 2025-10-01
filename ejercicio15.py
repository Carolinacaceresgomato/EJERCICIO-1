# ejercicio15.py

# Ahora, un Punto puede pertenecer a varios Poligonos.
# Usamos composición bidireccional: cada Poligono tiene una lista de Puntos,
# y cada Punto tiene una lista de Poligonos a los que pertenece.

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.poligonos = []  # Polígonos a los que pertenece este punto

    def agregar_poligono(self, poligono):
        if poligono not in self.poligonos:
            self.poligonos.append(poligono)

    def __repr__(self):
        return f"Punto({self.x}, {self.y})"

class Poligono:
    def __init__(self, puntos=None):
        self.puntos = []
        if puntos:
            for punto in puntos:
                self.agregar_punto(punto)

    def agregar_punto(self, punto):
        if punto not in self.puntos:
            self.puntos.append(punto)
            punto.agregar_poligono(self)

    def __repr__(self):
        return f"Poligono({self.puntos})"

# Ejemplo de diagrama de objetos:
# Creamos puntos que comparten pertenencia a varios polígonos

p1 = Punto(0, 0)
p2 = Punto(1, 0)
p3 = Punto(1, 1)
p4 = Punto(0, 1)

# Polígono A usa p1, p2, p3
poligonoA = Poligono([p1, p2, p3])

# Polígono B usa p1, p3, p4 (p1 y p3 son compartidos)
poligonoB = Poligono([p1, p3, p4])

# Ahora p1 y p3 pertenecen a dos polígonos
print(poligonoA)
print(poligonoB)
print(p1.poligonos)
print(p3.poligonos)