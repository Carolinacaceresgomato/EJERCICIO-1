class Proyecto:
    """
    Representa un proyecto de desarrollo de software.
    Atributos:
        nombre (str): Nombre del proyecto.
        descripcion (str): Breve descripción del objetivo del proyecto.
        tecnologias (list[str]): Tecnologías principales utilizadas.
        equipo (list['MiembroEquipo']): Lista de miembros del equipo.
        metodologia (str): Metodología de trabajo (ej. Scrum, Kanban).
        duracion_meses (int): Duración estimada del proyecto en meses.
    """
    def __init__(self, nombre, descripcion, tecnologias, equipo, metodologia, duracion_meses):
        self.nombre = nombre
        self.descripcion = descripcion
        self.tecnologias = tecnologias
        self.equipo = equipo
        self.metodologia = metodologia
        self.duracion_meses = duracion_meses

class MiembroEquipo:
    """
    Representa a un miembro del equipo de proyecto.
    Atributos:
        nombre (str): Nombre del miembro.
        rol (str): Rol dentro del proyecto (ej. Desarrollador, QA, Líder de proyecto).
        experiencia_anos (int): Años de experiencia profesional.
        especialidad (str): Área principal de especialización.
    """
    def __init__(self, nombre, rol, experiencia_anos, especialidad):
        self.nombre = nombre
        self.rol = rol
        self.experiencia_anos = experiencia_anos
        self.especialidad = especialidad

class Tecnologia:
    """
    Representa una tecnología utilizada en el proyecto.
    Atributos:
        nombre (str): Nombre de la tecnología (ej. Python, Docker).
        tipo (str): Tipo de tecnología (lenguaje, framework, herramienta).
        version (str): Versión utilizada.
    """
    def __init__(self, nombre, tipo, version):
        self.nombre = nombre
        self.tipo = tipo
        self.version = version

# Ejemplo de uso:
if __name__ == "__main__":
    equipo = [
        MiembroEquipo("Ana", "Desarrollador Backend", 5, "Python"),
        MiembroEquipo("Luis", "QA", 3, "Pruebas automatizadas"),
        MiembroEquipo("Marta", "Líder de proyecto", 8, "Gestión ágil")
    ]
    tecnologias = [
        Tecnologia("Python", "Lenguaje", "3.11"),
        Tecnologia("Docker", "Herramienta", "24.0"),
        Tecnologia("React", "Framework", "18.2")
    ]
    proyecto = Proyecto(
        nombre="Sistema de Gestión de Inventario",
        descripcion="Aplicación web para controlar inventarios en tiempo real.",
        tecnologias=[t.nombre for t in tecnologias],
        equipo=equipo,
        metodologia="Scrum",
        duracion_meses=6
    )
    print(f"Proyecto: {proyecto.nombre}")
    print(f"Descripción: {proyecto.descripcion}")
    print(f"Tecnologías: {', '.join(proyecto.tecnologias)}")
    print(f"Metodología: {proyecto.metodologia}")
    print(f"Duración: {proyecto.duracion_meses} meses")
    print("Equipo:")
    for miembro in proyecto.equipo:
        print(f"  - {miembro.nombre} ({miembro.rol}, {miembro.especialidad}, {miembro.experiencia_anos} años experiencia)")