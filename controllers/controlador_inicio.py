class ControladorInicio:
    def __init__(self, app):
        self.app = app

    def mostrar_destinoCulinario(self):
        self.app.cambiar_frame(self.app.vista_destinoCulinario)

    def mostrar_mapa(self):
        self.app.cambiar_frame(self.app.vista_mapa)

    def mostrar_calificacion(self):
        self.app.cambiar_frame(self.app.vista_calificacion)
