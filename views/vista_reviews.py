import tkinter as tk
from tkinter import ttk
from models.review import Review


class VistaReview(tk.Frame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        # Frames

        self.frame_reviewslista = tk.Frame(self, width=300, height=300)
        self.frame_reviewslista.grid(row=0, column=0, pady=30)
        self.frame_reviews = tk.Frame(self, width=300, height=300)
        self.frame_reviews.grid(row=0, column=1, pady=30)

        self.frame_agregar = tk.Frame(self, width=300, height=300)
        self.frame_agregar.grid(row=1, pady=30)
        
        # Detalle de reviews
        self.lista_reviews = tk.Listbox(self.frame_reviewslista)
        self.actualizar_reviews()
        self.lista_reviews.grid()

        self.detalle_reviews = tk.Label(self.frame_reviews, text='')
        self.detalle_reviews.grid()

        self.regresar_calificaciones = tk.Button(self.frame_reviews, text='Regresar', command=self.controlador.regresar_atras)
        self.regresar_calificaciones.grid()
        # agregar review
        self.usuario = tk.Label(self.frame_agregar, text='Usuario: ')
        self.usuario.grid(row=0, column=0, pady=30)
        self.reviewtext = tk.Label(self.frame_agregar, text='Review: ')
        self.reviewtext.grid(row=1, column=0, pady=30)
        self.n = tk.StringVar()
        self.cb_usuario = ttk.Combobox(self.frame_agregar, width=27, textvariable=self.n)
        self.cb_usuario.config(
                width=27,
                state='readonly',
                textvariable=self.n,
                values = self.actualizar_usuario()
                )
        self.cb_usuario.grid(row=0, column=1, pady=30)

        self.review_var = tk.StringVar()
        self.review_entry = tk.Entry(self.frame_agregar, textvariable= self.review_var, font=('calibre',10,'normal'))
        self.review_entry.grid(row=1, column= 1, pady=30)
        self.subir = tk.Button(self.frame_agregar, text='Subir', command= self.subir)
        #self.agregar_review = tk.Button(self.frame_agregar, text='Agregar Review',command= self.controlador.agregar_review(review))
        self.subir.grid(row=3, column=2, pady=30)

    def imprimir(self,a):
        print(f'{a}')

    def subir(self):
        usr = self.n.get()
        review = self.review_var.get()
        print(f'review: {review}, usr: {usr}')
        self.review_var.set('')
        self.n.set('')

    def actualizar_usuario(self):
        usuariostr = []
        usuarios = self.controlador.obtener_usuarios()
        for usuario in usuarios:
            usuariostr.append(usuario.nombre)
            #print(f'Nombre: {usuario.nombre}')
        return usuariostr
        #return [usuario.nombre[usuario] for usuario in usuarios]

    def actualizar_reviews(self):
        reviews = self.controlador.obtener_reviews()
        self.lista_reviews.delete(0, tk.END)
        for review in reviews:
            self.lista_reviews.insert(tk.END, review.id)

        #self.controlador.agregar_review(review1)
    def mostrar_reviews(self, reviews):
        info = []
        str = ''
        for review in reviews:
            info += [f'Review {review.id}\n Comentario: {review.comentario}\n Calificacion: {review.calificacion}\n']
        self.detalle_reviews['text'] = str.join(info)
