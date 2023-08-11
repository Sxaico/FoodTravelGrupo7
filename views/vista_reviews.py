import tkinter as tk
from tkinter import ttk
from models.review import Review


class VistaReview(tk.Frame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        # Frames
        self.frame_reviewslista = tk.Frame(self, width=500, height=250)
        self.frame_reviewslista.grid(row=0, column=0,pady=3)

        self.frame_reviews = tk.Frame(self, width=250, height=250)
        self.frame_reviews.grid(row=1, column=1, pady=3)

        self.frame_agregar = tk.Frame(self, width=250, height=250)
        self.frame_agregar.grid(row=1, column= 0, pady=3)
        
        #columns = ('review', 'usuario', 'comentario', 'animo')
        #self.tree = ttk.Treeview(self.frame_reviewslista, columns=columns, show='headings')
        #self.tree.heading('review', text='Review')
        #self.tree.heading('usuario', text='Usuario')
        #self.tree.heading('comentario', text='Comentario')
        #self.tree.heading('animo', text='Animo')       
        #self.tree.grid()
        # Detalle de reviews
        #self.lista_reviews = tk.Listbox(self.frame_reviewslista)
        #self.actualizar_reviews()
        #self.lista_reviews.grid(row=0, column=0)

        self.detalle_reviews = tk.Label(self.frame_reviewslista, text='', justify='left')
        self.detalle_reviews.grid()

        # Boton volver a calificaciones
        self.regresar_calificaciones = tk.Button(self.frame_agregar, text='Regresar', command=self.controlador.regresar_atras)
        self.regresar_calificaciones.grid(row=4, column=1)

        # agregar review
        self.usuario = tk.Label(self.frame_agregar, text='Usuario: ')
        self.usuario.grid(row=1,column=0)
        self.comentariotext = tk.Label(self.frame_agregar, text='Review: ')
        self.comentariotext.grid(row=2,column=0)
        self.animotxt = tk.Label(self.frame_agregar, text='Animo: ')
        self.animotxt.grid(row=3, column=0)

        # StringVar para los campos de la review 
        self.usrstr = tk.StringVar()
        self.comentario_var = tk.StringVar()
        self.calificacionstr = tk.StringVar()
        self.animostr = tk.StringVar()

        # Combobox Usuario
        self.cb_usuario = ttk.Combobox(self.frame_agregar, width=27, textvariable=self.usrstr)
        self.cb_usuario.config(
                width=27,
                state='readonly',
                textvariable=self.usrstr,
                values = self.actualizar_usuario()
                )
        self.cb_usuario.grid(row=1,column=1)

        # Combobox animo
        self.cb_animo = ttk.Combobox(self.frame_agregar, width=27, textvariable=self.animostr)
        self.cb_animo.config(
                width=27,
                state='readonly',
                textvariable=self.animostr,
                values = ['Positivo', 'Negativo']
                )
        self.cb_animo.grid(row=3,column=1)

        # comentario
        self.comentario_entry = tk.Entry(self.frame_agregar, textvariable= self.comentario_var, font=('calibre',10,'normal'), width=27)
        self.comentario_entry.grid(row=2,column=1)

        # Estrellas para calificacion
        values = {'★☆☆☆☆': '1',
                  '★★☆☆☆': '2',
                  '★★★☆☆': '3',
                  '★★★★☆': '4',
                  '★★★★★': '5'}

        # loop para crear los botones
        for text, value in values.items():
            tk.Radiobutton(self.frame_agregar,
                           text=text, variable=self.calificacionstr,
                           value=value, indicatoron=0,
                           background='light blue', width=10).grid(row=value, column=3)

        #Boton para subir comentario
        self.subir = tk.Button(self.frame_agregar, text='Subir', command=self.armar_review)
        self.subir.grid(row=5, column=1, pady=3)


    def armar_review(self):
        usr = self.usrstr.get()
        comentario = self.comentario_var.get()
        calificacion = self.calificacionstr.get()
        animo = self.animostr.get()
        destino_nombre = self.destino.nombre
        destino_id = self.destino.id
        usuario_id = 0
        for usuario in self.usuarios:
            if usr == usuario.nombre:
                usuario_id = usuario.id
        nueva_review = Review(1,destino_id,usuario_id, calificacion, comentario, animo)
        res = tk.messagebox.askyesno('Confirmar Review','Está seguro de que quiere subir esta review?')

        print(res)
        if res is True:
            Review.agregar_review('data/review.json', nueva_review)

        self.comentario_var.set('')
        self.usrstr.set('')
        self.calificacionstr.set('')
        self.animostr.set('')

    def actualizar_usuario(self):
        usuariostr = []
        self.usuarios = self.controlador.obtener_usuarios()
        for usuario in self.usuarios:
            usuariostr.append(usuario.nombre)
        return usuariostr

    def actualizar_reviews(self):
        reviews = self.controlador.obtener_reviews()
        self.lista_reviews.delete(0, tk.END)
        for review in reviews:
            self.lista_reviews.insert(tk.END, review)

    def mostrar_reviews(self, reviews, destino):
        info = []
        self.destino = destino
        str = ''
        for review in reviews:
            info += [f'Review {review.id}\n Comentario: {review.comentario}\n Calificacion: {review.calificacion}\n']
        self.detalle_reviews['text'] = str.join(info)
