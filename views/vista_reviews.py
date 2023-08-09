import tkinter as tk
from models.review import Review


class VistaReview(tk.Frame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        # Frames

        self.frame_reviews = tk.Frame(self, width=300, height=300)
        self.frame_reviews.grid()
        
        # Detalle de reviews
        self.detalle_reviews = tk.Label(self.frame_reviews, text='')
        self.detalle_reviews.grid()

        self.regresar_calificaciones = tk.Button(self.frame_reviews, text='Regresar', command=self.controlador.regresar_atras)
        self.regresar_calificaciones.grid()


        #self.controlador.agregar_review(review1)
    def mostrar_reviews(self, review):
        info = f'Comentario: {review.comentario}\n Calificacion: {review.calificacion}\n'
        self.detalle_reviews['text'] = info
