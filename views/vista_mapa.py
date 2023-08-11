import tkinter as tk
from tkintermapview import TkinterMapView

class VistaMapa(tk.Frame):
    def __init__(self, app=None, controlador=None, seleccionar_ubicacion_callback=None):
        super().__init__(app)
        self.app = app
        self.controlador = controlador
        self.seleccionar_ubicacion_callback = seleccionar_ubicacion_callback

        # Frames
        self.lbl = tk.LabelFrame(self)
        self.lbl.grid(row=0, column=1)
        self.lbl_destino = tk.LabelFrame(self, width=250, height=500)
        self.lbl_destino.grid(row=0, column=0)


        self.mapa = TkinterMapView(self.lbl, width=250, height=500, corner_radius=0)
        self.mapa.set_position(-24.789155036592028, -65.410273174454870)
        self.mapa.set_zoom = 16
        self.mapa.grid()

        self.lista_destino = tk.Listbox(self.lbl_destino)
        self.actualizar_destinos()
        self.lista_destino.grid()
        self.lista_destino.bind('<<ListboxSelect>>', self.seleccionar_destino)

        self.btn_volver = tk.Button(self.lbl_destino, text='Volver al inicio', command=self.controlador.volver_inicio)
        self.btn_volver.grid()

    def actualizar_destinos(self):
        destinos = self.controlador.obtener_destinos()
        self.lista_destino.delete(0, tk.END)
        for destino in destinos:
            self.lista_destino.insert(tk.END, destino.nombre)
    
    def obtener_indice(self):
        indice = self.lista_destino.curselection()
        if indice:
            return indice[0]
        else:
            return None
    
    def seleccionar_destino(self, event):
        return self.controlador.seleccionar_destino()

    def agregar_marcador_mapa(self, latitud, longitud, texto, imagen=None):
        return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen, command=self.seleccionar_ubicacion_callback)