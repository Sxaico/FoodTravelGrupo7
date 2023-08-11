class ControladorBusqueda:
    def __init__(self, app, destinos):
        self.app = app
        self.destinos = destinos
    
    def obtener_destinos(self):
        return self.destinos

    def volver_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)

