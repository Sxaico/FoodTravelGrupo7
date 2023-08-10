
#Vista Informacion
import tkinter as tk 

class VistaInfo(tk.Frame):
    def __init__(self, master= None, controlador=None):
        super().__init__(master)
        self.master =master
        self.controlador = controlador
        self.busqueda_label = tk.Label(self, text="")
        self.busqueda_label.pack(pady=50)
        self.busqueda_label.config (justify=tk.LEFT)
        self.boton_regresar= tk.Button(self, text= "Regresar al inicio", command=self.controlador.regresar_inicio)
        self.boton_regresar.pack(pady=10)
        
    def mostrar_info_busqueda(self, busqueda):
        info = f"Nombre: {busqueda.nombre}\ntipo de cocina: {busqueda.tipo_cocina}\n Ingredientes {busqueda.ingredientes}\nPrecio minimo {busqueda.precio_minimo}\nPrecio maximo: {busqueda.precio_maximo}\nPopularidad: {busqueda.popularidad}\nDisponibilidad: {busqueda.disponibilidad}\n ubicacion: {busqueda.id_ubicacion}\n"
        self.busqueda_label["text"]= info