import tkinter as tk
from tkinter.font import Font


class VistaInicio(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de inicio.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        # Define una fuente grande y en negrita para el título
        titulo_font = Font(size=24, weight="bold")

        # Crea una etiqueta para el título y la agrega a la vista
        self.titulo = tk.Label(self, text="Destinos culinarios disponibles", font=titulo_font)
        self.titulo.grid(row=0, column=0, pady=5)

        # Define una fuente más pequeña para la descripción de la funcionalidad
        descripcion_font = Font(size=12)

        # Crea una etiqueta para la descripción de la funcionalidad y la agrega a la vista
        self.descripcion = tk.Label(
            self,
            text="Aquí puedes ver ver los destinos culinarios con información detallada.",
            font=descripcion_font,
            wraplength=300,
        )
        self.descripcion.grid(row=1, column=0, pady=50)

        # Crea el botón para ir a destinos y lo agrega a la vista
        self.boton_destinos = tk.Button(
            self, text="Mostrar destinos culinarios", command=self.controlador.mostrar_destinoCulinario
        )
        self.boton_destinos.grid(row=2, column=0, pady=10)

        # Crea el botón para ir a destinos y lo agrega a la vista
        self.boton_mapa = tk.Button(
            self, text="Mostrar mapas", command=self.controlador.mostrar_mapa
        )
        self.boton_mapa.grid(row=3, column=1, pady=10)

