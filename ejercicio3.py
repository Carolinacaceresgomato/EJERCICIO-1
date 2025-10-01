# Definición de clases para el diagrama de objetos

class Persona:
    def __init__(self, nombre, apellido, apellido_soltera=None):
        self.nombre = nombre
        self.apellido = apellido
        self.apellido_soltera = apellido_soltera
        self.pareja = None
        self.hijos = []
        self.padres = []

    def casar_con(self, otra_persona):
        self.pareja = otra_persona
        otra_persona.pareja = self

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)
        hijo.padres.append(self)

# Crear objetos según el texto

# Padres
carlos = Persona("Carlos", "Windsor")
diana = Persona("Diana", "de Gales", apellido_soltera="Spencer")
carlos.casar_con(diana)

# Hijo
guillermo = Persona("Guillermo", "Windsor")
carlos.agregar_hijo(guillermo)
diana.agregar_hijo(guillermo)

# Esposa de Guillermo
kate = Persona("Kate", "Windsor", apellido_soltera="Middleton")
guillermo.casar_con(kate)

# Visualización simple de relaciones
def mostrar_familia(persona):
    print(f"{persona.nombre} {persona.apellido}", end="")
    if persona.apellido_soltera:
        print(f" (nacida {persona.apellido_soltera})", end="")
    if persona.pareja:
        print(f" está casado/a con {persona.pareja.nombre} {persona.pareja.apellido}", end="")
    print()
    if persona.padres:
        print("  Padres:")
        for padre in persona.padres:
            print(f"    - {padre.nombre} {padre.apellido}")
    if persona.hijos:
        print("  Hijos:")
        for hijo in persona.hijos:
            print(f"    - {hijo.nombre} {hijo.apellido}")

# Ejemplo de uso:
mostrar_familia(guillermo)