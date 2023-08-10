# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 17:57:40 2023

@author: sofia
"""

class ControladorBusqueda:
    def __init__(self,app):
        self.app =app
        
    def regresar_juegos(self):
        self.app.cambiar_frame(self.app.vista_)