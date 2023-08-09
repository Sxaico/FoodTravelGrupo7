import json


class Usuario:
    def __init__(self, id:int, nombre:str, apellido:str, historial_rutas:list[int]): 
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.historial_rutas = historial_rutas

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
        return [Usuario.de_json(json.dumps(dato)) for dato in datos]
