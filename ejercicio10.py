from typing import List

# ejercicio10.py


class MiembroEquipo:
    def __init__(self, nombre: str, rol: str, experiencia: int):
        self.nombre = nombre
        self.rol = rol
        self.experiencia = experiencia  # años de experiencia

    def __str__(self):
        return f"{self.nombre} ({self.rol}, {self.experiencia} años exp.)"

class Proyecto:
    def __init__(
        self,
        nombre: str,
        descripcion: str,
        tecnologias: List[str],
        equipo: List[MiembroEquipo],
        metodologia: str,
        duracion_meses: int
    ):
        self.nombre = nombre
        self.descripcion = descripcion
        self.tecnologias = tecnologias
        self.equipo = equipo  # Asociación: lista de objetos MiembroEquipo
        self.metodologia = metodologia
        self.duracion_meses = duracion_meses

    def agregar_miembro(self, miembro: MiembroEquipo):
        self.equipo.append(miembro)

    def listar_equipo(self):
        return [str(miembro) for miembro in self.equipo]

# Ejemplo de uso:
if __name__ == "__main__":
    miembro1 = MiembroEquipo("Ana", "Desarrolladora", 5)
    miembro2 = MiembroEquipo("Luis", "Scrum Master", 3)
    equipo = [miembro1, miembro2]

    proyecto = Proyecto(
        nombre="Sistema de Gestión",
        descripcion="Plataforma para gestionar proyectos empresariales.",
        tecnologias=["Python", "Django", "PostgreSQL"],
        equipo=equipo,
        metodologia="Scrum",
        duracion_meses=8
    )

    print("Equipo del proyecto:")
    for m in proyecto.listar_equipo():
        print(m)