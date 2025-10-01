class Persona:
    def __init__(self, nombre, apellido1, apellido2, fecha_nacimiento, sexo, numero_identificacion):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.fecha_nacimiento = fecha_nacimiento  # Formato sugerido: 'YYYY-MM-DD'
        self.sexo = sexo  # Ejemplo: 'M' o 'F'
        self.numero_identificacion = numero_identificacion