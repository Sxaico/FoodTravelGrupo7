from models.review import Review
from models.usuario import Usuario


class ControladorReview:
    def __init__(self, app):
        self.app = app

    def regresar_atras(self):
        self.app.cambiar_frame(self.app.vista_calificacion)

    def agregar_review(self, review):
        Review.agregar_review('data/review.json', review)

    def obtener_reviews(self):
        self.reviews = Review.cargar_de_json('data/review.json')
        return self.reviews

    def obtener_usuarios(self):
        self.usuario = Usuario.cargar_de_json('data/usuario.json')
        return self.usuario
