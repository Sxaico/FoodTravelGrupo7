import tkinter as tk


class VistaInfo(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de la información de un destino.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.destino_label = tk.Label(self, text="")
        self.destino_label.grid(pady=50)
        self.destino_label.config(justify=tk.LEFT)
        self.boton_regresar = tk.Button(
            self,
            text="Regresar a la lista de destinos",
            command=self.controlador.regresar_destinos_culinarios,
        )
        self.boton_regresar.grid(pady=10)

    def mostrar_info_destino_culinario(self, destino):
        """
        Muestra la información del destino recibido como parámetro.
        """
        info = f"Destino: {destino.nombre}\nTipo de cocina: {destino.tipo_cocina}\nPrecio minimo: {destino.precio_minimo}\nPrecio maximo: {destino.precio_maximo}\nPopularidad: {destino.popularidad}"
        self.destino_label["text"] = info
