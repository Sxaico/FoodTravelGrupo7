# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 18:46:45 2023

@author: sofia
"""
import json

class BusqAvanz:
    def __init__(self, nombre, tipo_cocina, ingredientes, precio_minimo,precio_maximo,popularidad,disponibilidad, id_ubicacion):
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.infredientes = ingredientes
        self.precio_minimo = precio_minimo
        self.precio_maximo =precio_maximo
        self.popularidad = popularidad
        self.disponibilidad = disponibilidad
        self.id_ubicacion = id_ubicacion
        
    @classmethod
    def cargar_de_json(cls, archivo):
        with open( archivo,'r') as f:
            data =json.load(f)
        return [cls(**modelbusqavanz) for modelbusqavanz in data]
                 
        