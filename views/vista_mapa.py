import tkinter as tk
from tkinter import ttk
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk


class VistaPrincipalMapa(tk.Frame):
    def __init__(self, app=None, controlador=None, seleccionar_destino_callback=None, seleccionar_ubicacion_callback=None):
        super().__init__(app)
        self.app = app
        self.controlador = controlador
        self.seleccionar_destino_callback = seleccionar_destino_callback
        self.seleccionar_ubicacion_callback = seleccionar_ubicacion_callback

        # Frame para mapa
        self.frame_mapa = tk.Frame(self, width=800, height=600)
        self.frame_mapa.grid(row=0,column=1, pady=10)

        self.mapa = TkinterMapView(self.frame_mapa, width=800, height=600, corner_radius=0)
        #self.mapa.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.mapa.set_position(-24.789116075505337, -65.41027317448516)
        self.mapa.set_zoom(16)
        self.mapa.grid(pady=10)

        # Frame para listbox
        self.frame_destinos = tk.Frame(self, height=600, width=600)
        self.frame_destinos.grid(row=0, column=0, pady=10)

        # Listbox para las ubicaciones
        self.lista_destinos = tk.Listbox(self.frame_destinos)
        self.lista_destinos.config(width=30)
        self.lista_destinos.bind('<<ListboxSelect>>', self.seleccionar_destino_callback)
        self.lista_destinos.grid()

    def agregar_destino(self, destino):
        print(f'{destino.nombre}')
        self.nombre = destino.nombre
        self.lista_destinos.insert(tk.END, destino.nombre)

    #def agregar_destino(self):
    #    self.lista_destinos.delete(0, tk.END)
    #    destino = self.controlador.obtener_destinos()
    #    self.nombre = destino.nombre
    #    for destino in destino:
    #        self.lista_destinos.insert(tk.END, destino.nombre)

    def agregar_marcador_mapa(self, latitud, longitud, texto, imagen=None):
        return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen, command=self.seleccionar_ubicacion_callback)

    def obtener_indice(self):
        indice = self.lista_destinos.curselection()
        if indice:
            return indice[0]
        else:
            return None
