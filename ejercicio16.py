class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.padres = []      # Asociación: 0..2 padres (rol: padre/madre)
        self.hijos = []       # Asociación: 0..* hijos (rol: hijo/hija)
        self.hermanos = []    # Asociación: 0..* hermanos (rol: hermano/hermana)
        self.pareja = None    # Asociación: 0..1 pareja (rol: pareja)

    def agregar_padre(self, padre):
        if len(self.padres) < 2 and padre not in self.padres:
            self.padres.append(padre)
            padre.hijos.append(self)

    def agregar_hijo(self, hijo):
        if hijo not in self.hijos:
            self.hijos.append(hijo)
            hijo.padres.append(self)

    def agregar_hermano(self, hermano):
        if hermano != self and hermano not in self.hermanos:
            self.hermanos.append(hermano)
            hermano.hermanos.append(self)

    def establecer_pareja(self, pareja):
        if self.pareja is not pareja:
            self.pareja = pareja
            pareja.pareja = self