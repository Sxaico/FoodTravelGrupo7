import tkinter as tk


class VistaDestinosCulinarios(tk.Frame):
    def __init__(self, master=None, controlador=None):
        '''
        Crear la vista para explorar los distintos destinos culinarios
        '''
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        self.titulo = tk.Label(self, text='Lista de los destinos culinarios disponibles')
        self.titulo.pack(pady=10)

        self.listbox = tk.Listbox(self)
        self.listbox.config(width=50)

        self.listbox.bind('<Double-Button-1>', self.seleccionar_destino_culinario)

        self.listbox.pack(pady=10)
        self.actualizar_destinos_culinarios()

        self.boton_inicio = tk.Button(
                self, text='Ir a inicio', command=self.controlador.regresar_inicio
                )
        self.boton_inicio.pack(pady=10)

        def actualizar_destinos_culinarios(self):
            destinos_culinarios = self.controlador.obtener_destinos_culinarios()
            self.listbox.delete(0, tk.END)
            for destino_culinario in destinos_culinarios:
                self.listbox.insert(tk.END, destino_culinario.nombre)

        def obtener_destinos_culinarios(self):
            indice = self.listbox.curselection()
            if indice:
                return indice[0]
            else:
                return None

        def seleccionar_destino_culinario(self, event):
            self.controlador.seleecionar_destino_culinario()
