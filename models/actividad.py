import json
class Actividad:
    def __init__(self, nombre: str, destino_id: int, hora_inicio: str):
        self.nombre = nombre
        self.destino_id = destino_id
        self.hora_inicio = hora_inicio

    def to_json(self):
        return{"nombre": self.nombre, "destino_id": self.destino_id, "hora_inicio": self.hora_inicio}

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(data["nombre"], data["destino_id"], data["hora_inicio"])
    