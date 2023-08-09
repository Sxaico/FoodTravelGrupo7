from models.review import Review


class ControladorReview:
    def __init__(self, app):
        self.app = app

    def regresar_atras(self):
        self.app.cambiar_frame(self.app.vista_calificacion)

    def agregar_review(self, review):
        Review.agregar_review('data/review.json', review)
