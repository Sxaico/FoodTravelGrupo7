from models.destinoCulinario import DestinoCulinario
from models.review import Review


class ControladorCalificacion:
    def __init__(self, app):
        self.app = app
        self.review = Review.cargar_de_json('data/review.json')

    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)

    def ir_reviews(self):
        ids_reviews = []
        indice = self.app.vista_calificacion.obtener_indice_destinos()
        if indice is not None:
            destino_seleccionado = self.destinos[indice]
            review_seleccionada = Review(0,0,0,0,'','')

            for review in self.review:
                if review.id_destino == destino_seleccionado.id:
                    ids_reviews.append(review.id)
                    review_seleccionada = review
                    self.app.vista_review.mostrar_reviews(review_seleccionada)
                    print(f'ids_reviews: {ids_reviews}')
                    #break
            #self.app.vista_review.mostrar_reviews(ids_reviews)
            #review = review_seleccionada[review_seleccionada.id]
            self.app.cambiar_frame(self.app.vista_review)


    def obtener_destinos(self):
        self.destinos = DestinoCulinario.cargar_de_json('data/destinos_culinarios.json')
        return self.destinos

    def seleccionar_destino(self):
        indice = self.app.vista_calificacion.obtener_indice_destinos()
        print(f'indice: {indice}')
        if indice is not None:
            destino = self.destinos[indice]
            self.app.vista_info_destinos.mostrar_info_destino_culinario(destino)
            self.app.cambiar_frame(self.app.vista_info_destinos)

    def seleccionar_destino2(self):
        indice = self.app.vista_calificacion.obtener_indice_destinos()
        if indice is not None:
            destino = self.destinos[indice]
            self.app.vista_calificacion.mostrar_destino_frame(destino)
