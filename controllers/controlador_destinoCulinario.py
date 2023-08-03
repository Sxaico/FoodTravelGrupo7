class ControladorDestinoCulinario:
    def __init__(self, app, modelo_destino_culinario):
        self.app = app
        self.modelo_destino_culinario = modelo_destino_culinario

    def obtener_destinos_culinarios(self):
        return self.modelo_destino_culinario

    def seleccionar_destino_culinario(self):
        """
        Obtiene el índice del juego seleccionado y llama a la vista de
        información para mostrar la información del juego.
        """
        indice = self.app.vista_destinoCulinario.obtener_destinos_culinarios()
        if indice is not None:
            destino_culinario = self.modelo_destino_culinario[indice]
            self.app.vista_info_destinos.mostrar_info_destino_culinario(destino_culinario)
            self.app.cambiar_frame(self.app.vista_info_destinos)

    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)
