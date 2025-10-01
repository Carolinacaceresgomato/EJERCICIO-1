

class Catedral:
    def __init__(self, nombre, ubicacion, inicio_construccion, materiales, estilos, consagraciones, bien_interes_cultural):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.inicio_construccion = inicio_construccion
        self.materiales = materiales
        self.estilos = estilos
        self.consagraciones = consagraciones
        self.bien_interes_cultural = bien_interes_cultural

class Ubicacion:
    def __init__(self, ciudad, provincia, region, pais):
        self.ciudad = ciudad
        self.provincia = provincia
        self.region = region
        self.pais = pais

class Consagracion:
    def __init__(self, fecha, descripcion):
        self.fecha = fecha
        self.descripcion = descripcion

# Instanciación de objetos según la descripción

ubicacion = Ubicacion(
    ciudad="Santiago de Compostela",
    provincia="La Coruña",
    region="Galicia",
    pais="España"
)

consagraciones = [
    Consagracion(fecha=1128, descripcion="Primera consagración"),
    Consagracion(fecha="3 de abril de 1211", descripcion="Consagración definitiva")
]

catedral = Catedral(
    nombre="Catedral de Santiago de Compostela",
    ubicacion=ubicacion,
    inicio_construccion=1075,
    materiales=["granito"],
    estilos=["románico", "gótico", "barroco", "plateresco", "neoclásico"],
    consagraciones=consagraciones,
    bien_interes_cultural=1896
)
