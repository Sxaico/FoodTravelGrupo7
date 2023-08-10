import tkinter as tk


class VistaCalificacion(tk.Frame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        # Frames
        self.frame_destinos = tk.Frame(self, width=300, height=300)
        self.frame_destinos.grid(row=0, column=0)
        self.frame_detalle = tk.Frame(self, width=300, height=300)
        self.frame_detalle.grid(row=0, column=1)

        self.texto = tk.Label(self.frame_destinos, text='hola esto esta en el frame_destinos')
        self.texto.grid()
        self.texto2 = tk.Label(self.frame_detalle, text='Esto esta en frame2')
        self.texto2.grid()

        self.calificacion = tk.Label(self.frame_detalle, text='')
        self.calificacion.grid()

        self.lista_destinos = tk.Listbox(self.frame_destinos, width=15, height=10,activestyle='dotbox')
        self.actualizar_destinos()
        self.lista_destinos.grid(pady=50)
        self.lista_destinos.bind('<<ListboxSelect>>', self.seleccionar_destino2)

        # Regresar
        self.volver_inicio = tk.Button(self.frame_destinos, text='Volver al inicio', command=self.controlador.regresar_inicio)
        self.volver_inicio.grid()

        # Ir a Rewviews
        self.ir_reviews = tk.Button(self.frame_detalle, text='Ir a reviews', command=self.controlador.ir_reviews)
        self.ir_reviews.grid(row=2, column=0, pady=10)

    def actualizar_destinos(self):
        destinos = self.controlador.obtener_destinos()
        self.lista_destinos.delete(0, tk.END)
        for destino in destinos:
            self.lista_destinos.insert(tk.END, destino.nombre)

    def obtener_indice_destinos(self):
        indice = self.lista_destinos.curselection()
        if indice:
            return indice[0]
        else:
            return None

    def seleccionar_destino(self, event):
        return self.controlador.seleccionar_destino()

    def seleccionar_destino2(self, event):
        return self.controlador.seleccionar_destino2()

    def mostrar_destino_frame(self, destino):
        info = f'Nombre: {destino.nombre}\n Popularidad: {destino.popularidad}\n'
        self.texto2['text'] = info
