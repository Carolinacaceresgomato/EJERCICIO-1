# Propuesta de diagrama de clases en Python (sin diagrama visual, solo clases y relaciones)
# Basado en un ejemplo típico de diagrama de objetos (ajusta los nombres según tu ejercicio2.py)

class Persona:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.cursos = []  # Asociación: una persona puede estar en varios cursos

    def inscribir_en_curso(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.agregar_estudiante(self)

class Curso:
    def __init__(self, nombre: str, profesor):
        self.nombre = nombre
        self.profesor = profesor  # Asociación: un curso tiene un profesor
        self.estudiantes = []     # Asociación: un curso tiene varios estudiantes

    def agregar_estudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)

class Profesor(Persona):
    def __init__(self, nombre: str):
        super().__init__(nombre)
        self.cursos_dictados = []  # Asociación: un profesor puede dictar varios cursos

    def dictar_curso(self, curso):
        if curso not in self.cursos_dictados:
            self.cursos_dictados.append(curso)

# Ejemplo de asociaciones y cardinalidades:
# - Una Persona puede estar en 0..* Cursos (rol: estudiante)
# - Un Curso tiene 1 Profesor (rol: profesor)
# - Un Curso tiene 0..* Personas (rol: estudiantes)
# - Un Profesor puede dictar 0..* Cursos

# Nota: Para un diagrama visual, puedes usar herramientas como draw.io o UMLet.