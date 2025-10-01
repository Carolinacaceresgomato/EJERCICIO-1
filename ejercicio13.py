class Poligono:
    def __init__(self, puntos):
        if len(puntos) < 3:
            raise ValueError("Un polígono debe tener al menos 3 puntos")
        self.puntos = puntos  # Lista de tuplas (x, y)

    def __str__(self):
        return f"Polígono con puntos: {self.puntos}"

# Ejemplo: cuadrado con vértices en (0,0), (0,1), (1,1), (1,0)
cuadrado = Poligono([(0, 0), (0, 1), (1, 1), (1, 0)])
print(cuadrado)