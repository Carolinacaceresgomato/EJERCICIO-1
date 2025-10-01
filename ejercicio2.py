# Diagrama de objetos en Python para la réplica de "La Gioconda"

class ObraDeArte:
    def __init__(self, titulo, autor, fecha, tecnica, subtecnica, soporte, descripcion, estado_conservacion, original=None):
        self.titulo = titulo
        self.autor = autor
        self.fecha = fecha
        self.tecnica = tecnica
        self.subtecnica = subtecnica
        self.soporte = soporte
        self.descripcion = descripcion
        self.estado_conservacion = estado_conservacion
        self.original = original

# Obra original
gioconda_original = ObraDeArte(
    titulo="La Gioconda",
    autor="Leonardo Da Vinci",
    fecha="1503-1516",
    tecnica="óleo",
    subtecnica="sfumato",
    soporte="madera de álamo",
    descripcion="Obra maestra expuesta en el Museo Louvre de París.",
    estado_conservacion="regular"
)

# Réplica estudiada
gioconda_replicada = ObraDeArte(
    titulo="La Gioconda (réplica del Prado)",
    autor="Anónimo (alumno de la escuela de Leonardo)",
    fecha="1503-1516",
    tecnica="óleo",
    subtecnica="pincelada simple",
    soporte="madera de nogal",
    descripcion=(
        "Réplica más antigua conocida, procedente de las Colecciones Reales, "
        "expuesta en el Museo del Prado. Realizada por un discípulo de Leonardo "
        "contemporáneamente a la original. Mejor estado de conservación que la original."
    ),
    estado_conservacion="muy bueno",
    original=gioconda_original
)

# Visualización simple de relaciones
def mostrar_diagrama(obj):
    print(f"Título: {obj.titulo}")
    print(f"Autor: {obj.autor}")
    print(f"Fecha: {obj.fecha}")
    print(f"Técnica: {obj.tecnica}")
    print(f"Sub-técnica: {obj.subtecnica}")
    print(f"Soporte: {obj.soporte}")
    print(f"Estado de conservación: {obj.estado_conservacion}")
    print(f"Descripción: {obj.descripcion}")
    if obj.original:
        print("\n--- Basada en la obra original ---")
        mostrar_diagrama(obj.original)

if __name__ == "__main__":
    mostrar_diagrama(gioconda_replicada)