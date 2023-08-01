class ControladorInicio:
    def __init__(self, app):
        self.app = app

    def mostrar_destinoCulinario(self):
        self.app.cambiar_frame(self.vista_destinoCulinario)
