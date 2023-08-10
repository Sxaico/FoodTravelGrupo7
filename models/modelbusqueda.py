# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 18:16:59 2023

@author: sofia
"""

#model Busqueda por nombre
import json 

class Busqueda:
    def __init__(self,nombre):
        self.nombre= nombre
        
        
    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo,'r') as f:
            data= json.load(f)
            return [cls(**modelbusqueda) for modelbusqueda in data]