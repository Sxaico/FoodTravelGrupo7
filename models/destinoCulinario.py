import json


class DestinoCulinario:
    def __init__(self, id:int, nombre: str, tipo_cocina: str, ingredientes: list[str], precio_minimo: float, precio_maximo: float, popularidad: float, disponibilidad: bool, id_ubicacion: int, imagen: str):
        self.id = id
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes
        self.precio_minimo = precio_minimo
        self.precio_maximo = precio_maximo
        self.popularidad = popularidad
        self.disponibilidad = disponibilidad
        self.id_ubicacion = id_ubicacion
        self.imagen = imagen

    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**destino_culinario) for destino_culinario in data]


'''
    def to_json(self):
        return{"nombre": self.nombre, "tipo_cocina": self.tipo_cocina, "ingredientes": self.ingredientes, "precio_minimo": self.precio_minimo, "precio_maximo": self.precio_maximo,"popularidad": self.popularidad,"disponibilidad": self.disponibilidad,"id_ubicacion": self.id_ubicacion,"imagen": self.imagen}
''' 
