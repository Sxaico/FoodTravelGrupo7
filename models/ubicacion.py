import json


class Ubicacion:
    def __init__(self, id:int, direccion: str, coordenadas: list[int]):
        self.id = id
        self.direccion = direccion
        self.coordenadas = coordenadas

    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**ubicacion) for ubicacion in data]
