from datetime import date, timedelta

class Libro:
    def __init__(self, id_libro, titulo, tematica):
        self.id_libro = id_libro
        self.titulo = titulo
        self.tematica = tematica
        self.ejemplares = []

    def agregar_ejemplar(self, ejemplar):
        self.ejemplares.append(ejemplar)

class Ejemplar:
    def __init__(self, id_ejemplar):
        self.id_ejemplar = id_ejemplar
        self.prestamo = None

class Prestamo:
    def __init__(self, lector, fecha_prestamo, dias_maximos):
        self.lector = lector
        self.fecha_prestamo = fecha_prestamo
        self.fecha_entrega = fecha_prestamo + timedelta(days=dias_maximos)
        self.devuelto = False

    def marcar_devuelto(self):
        self.devuelto = True

    def esta_vencido(self, fecha_actual):
        return not self.devuelto and fecha_actual > self.fecha_entrega

class Lector:
    def __init__(self, id_lector, nombre, direccion):
        self.id_lector = id_lector
        self.nombre = nombre
        self.direccion = direccion
        self.penalizaciones = 0

    def aplicar_penalizacion(self):
        self.penalizaciones += 1

class Empleado(Lector):
    def __init__(self, id_empleado, nombre, direccion):
        super().__init__(id_empleado, nombre, direccion)

class Estanteria:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.libros = []

    def agregar_libro(self, libro):
        if len(self.libros) < self.capacidad:
            self.libros.append(libro)
            return True
        return False

class Planta:
    def __init__(self, numero, estanterias):
        self.numero = numero
        self.estanterias = estanterias  # lista de Estanteria

    def capacidad_total(self):
        return sum(e.capacidad for e in self.estanterias)

class Biblioteca:
    def __init__(self, plantas):
        self.plantas = plantas  # lista de Planta
        self.lectores = []
        self.empleados = []

    def capacidad_total(self):
        return sum(planta.capacidad_total() for planta in self.plantas)

    def registrar_lector(self, lector):
        self.lectores.append(lector)

    def registrar_empleado(self, empleado):
        self.empleados.append(empleado)