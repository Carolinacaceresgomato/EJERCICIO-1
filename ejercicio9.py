from enum import Enum, auto

class Cuadro(Enum):
    LA_GIOCONDA = auto()

class Persona(Enum):
    MONA_LISA = auto()

class Pintor(Enum):
    LEONARDO_DA_VINCI = auto()

class Lugar(Enum):
    FLORENCIA = auto()
    LOUVRE = auto()

class Tecnica(Enum):
    OLEO = auto()

class Soporte(Enum):
    TABLA_DE_ALAMO = auto()

class EstadoConservacion(Enum):
    BUENO = auto()

class Copias(Enum):
    SI = auto()
    NO = auto()

class ObraDeArte:
    def __init__(self, cuadro, representado, pintor, lugar_creacion, copias, tecnica, soporte, ubicacion_actual, estado):
        self.cuadro = cuadro
        self.representado = representado
        self.pintor = pintor
        self.lugar_creacion = lugar_creacion
        self.copias = copias
        self.tecnica = tecnica
        self.soporte = soporte
        self.ubicacion_actual = ubicacion_actual
        self.estado = estado

# Instancia representando La Gioconda (Mona Lisa)
gioconda = ObraDeArte(
    cuadro=Cuadro.LA_GIOCONDA,
    representado=Persona.MONA_LISA,
    pintor=Pintor.LEONARDO_DA_VINCI,
    lugar_creacion=Lugar.FLORENCIA,
    copias=Copias.SI,
    tecnica=Tecnica.OLEO,
    soporte=Soporte.TABLA_DE_ALAMO,
    ubicacion_actual=Lugar.LOUVRE,
    estado=EstadoConservacion.BUENO
)