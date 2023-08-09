import json

class Review:
    def __init__(self, id: int, id_destino: int, id_usuario: int, calificacion: int, comentario: str, animo: str):
        self.id = id
        self.id_destino = id_destino
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def a_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def agregar_review(archivo_json, nuevo_review):
        reviews = Review.cargar_de_json(archivo_json)
        reviews.append(nuevo_review)

        with open(archivo_json, 'w') as archivo:
            datos = [review.__dict__ for review in reviews]
            json.dump(datos, archivo, indent=4)

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)

    @staticmethod
    def cargar_de_json(archivo_json):
        with open(archivo_json, "r") as archivo:
            datos = json.load(archivo)
        return [Review.de_json(json.dumps(dato)) for dato in datos]
