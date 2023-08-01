import json

class Ruta_destino:
    def __init__(self, id: int, nombre: str, destinos: list[str]):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

    def to_json(self):
        return{'id': self.id, 'nombre': self.nombre, 'destinos': self.destinos}

    @classmethod
    def from_json(cls, json_data):
        data = json.load(json_data)
        return cls(data['id'], data['nombre'], data['destinos']) 
        
