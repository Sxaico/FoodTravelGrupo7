from models.review import Review

review1 = Review(id=1, id_destino=1, id_usuario=1, calificacion=10,comentario='Muy bueno',animo='Positivo')

Review.agregar_review('data/review.json', review1)
