from datetime import date

class ActuacionArqueologica:
    TIPOS_VALIDOS = {"sondeo", "excavación", "seguimiento"}

    def __init__(self, fecha_inicio: date, fecha_fin: date, tipo: str):
        if tipo.lower() not in self.TIPOS_VALIDOS:
            raise ValueError(f"Tipo inválido: {tipo}. Debe ser uno de {self.TIPOS_VALIDOS}")
        if fecha_fin < fecha_inicio:
            raise ValueError("La fecha de fin no puede ser anterior a la fecha de inicio.")
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.tipo = tipo.lower()

    def __str__(self):
        return (f"Actuación arqueológica ({self.tipo}): "
                f"del {self.fecha_inicio} al {self.fecha_fin}")