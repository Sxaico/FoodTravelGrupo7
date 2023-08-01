class ControladorInfo:
    def __init__(self, app):
        self.app = app

    def regresar_destinos_culinarios(self):
        self.app.cambiar_frame(self.app.vista_destinos_culinarios)
