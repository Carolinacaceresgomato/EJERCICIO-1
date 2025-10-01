from typing import List, Optional

class EstructuraArqueologica:
    def __init__(
        self,
        codigo: str,
        datacion: str,
        materiales: List[str],
        subestructuras: Optional[List['EstructuraArqueologica']] = None
    ):
        self.codigo = codigo
        self.datacion = datacion
        self.materiales = materiales
        self.subestructuras = subestructuras if subestructuras is not None else []

    def agregar_subestructura(self, subestructura: 'EstructuraArqueologica'):
        self.subestructuras.append(subestructura)