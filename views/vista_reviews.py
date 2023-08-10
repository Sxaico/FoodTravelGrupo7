import tkinter as tk
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
        
        # Detalle de reviews
        self.lista_reviews = tk.Listbox(self.frame_reviewslista)
        self.actualizar_reviews()
        self.lista_reviews.grid()

        self.detalle_reviews = tk.Label(self.frame_reviews, text='')
        self.detalle_reviews.grid()

        self.regresar_calificaciones = tk.Button(self.frame_reviews, text='Regresar', command=self.controlador.regresar_atras)
        self.regresar_calificaciones.grid()

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
        print(info)
        self.detalle_reviews['text'] = str.join(info)
