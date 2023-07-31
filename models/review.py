import json

class Review:
    def __init__(self, id: int, id_destino: int, id_usuadio: int, calificacion: int, comentario: str, animo: str):
        self.id = id
        self.id_destino = id_destino
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def to_json(self):
        return{'id': self.id, 'id_destino': self.id_destino, 'id_usuario': self.id_usuario, 'calificacion': self.calificacion, 'comentario': self.comentario, 'animo': self.animo}
    
    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(data['id'], data['id_destino'], data['id_usuario'], data['calificacion'], data['comentario'], data['animo'])
