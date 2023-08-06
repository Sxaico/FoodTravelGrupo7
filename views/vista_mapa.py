import tkinter as tk
from tkinter import ttk
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk


class VistaPrincipalMapa(tk.Frame):
    def __init__(self, root= None, controlador= None, seleccionar_destino_callback=None, seleccionar_ubicacion_callback=None):
        super().__init__(root)
        self.root = root
        self.controlador = controlador
        self.seleccionar_destino_callback = seleccionar_destino_callback
        self.seleccionar_ubicacion_callback = seleccionar_ubicacion_callback
        self.frame_mapa = tk.Frame(self.root, width=600, height=600)

        self.frame_destinos = tk.Frame(self.root, width=600, height=600)
        self.frame_destinos.grid(row=1, column=0, pady=10)

        self.mapa = TkinterMapView(self.frame_destinos, width=600, height=600)
        self.mapa.set_position(-24.789147136090282, -65.41028151131326)
        self.mapa.set_zoom(16)
        self.mapa.grid(row=1, column=1, pady=10)

        
        self.boton_regresar = tk.Button(
                self,
                text='Volver al inicio',
                command=self.controlador.regresar_inicio
                )
        self.boton_regresar.pack(pady=10)
       
        # Listbox para los destinos culinarios
        self.lista_destinos = tk.Listbox(self.frame_destinos)
        self.lista_destinos.bind('<<ListboxSelect>>', seleccionar_destino_callback)
        self.lista_destinos.grid(row=2, column=0, pady=10)

    def agregar_destino(self, destino):
        nombre = destino.nombre
        self.lista_destinos.insert(tk.END, nombre)

    def agregar_marcador_mapa(self, latitud, longitud, texto, imagen=None):
        return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen, command=self.seleccionar_ubicacion_callback)
