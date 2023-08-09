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

    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)

    @staticmethod
    def cargar_de_json(archivo_json):
        with open(archivo_json, "r") as archivo:
            datos = json.load(archivo)
        return [DestinoCulinario.de_json(json.dumps(dato)) for dato in datos]

'''
    def to_json(self):
        return{"nombre": self.nombre, "tipo_cocina": self.tipo_cocina, "ingredientes": self.ingredientes, "precio_minimo": self.precio_minimo, "precio_maximo": self.precio_maximo,"popularidad": self.popularidad,"disponibilidad": self.disponibilidad,"id_ubicacion": self.id_ubicacion,"imagen": self.imagen}
''' 
