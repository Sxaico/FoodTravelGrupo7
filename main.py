import tkinter as tk
from tkintermapview import TkinterMapView
# import customtkinter as ctk
from models.usuario import Usuario
from models.review import Review
from models.actividad import Actividad
from models.rutaDestinos import Ruta_destino
from models.destinoCulinario import DestinoCulinario
from models.ubicacion import Ubicacion
from views.vista_inicio import VistaInicio
from views.vista_destinoCulinario import VistaDestinosCulinarios
from views.vista_info_destinos import VistaInfo
from views.vista_calificacion import VistaCalificacion
from views.vista_mapa import VistaMapa
from controllers.controlador_inicio import ControladorInicio
from controllers.controlador_destinoCulinario import ControladorDestinoCulinario
from controllers.controlador_info_destinos import ControladorInfo
from controllers.controlador_calificacion import ControladorCalificacion
from controllers.controlador_mapa import ControladorMapa
from views.vista_reviews import VistaReview
from views.vista_busqueda import VistaBusqueda
from controllers.controlador_reviews import ControladorReview
from controllers.controlador_busqueda import ControladorBusqueda
#from views.vistaInfo import VistaInfo
#from controllers.controladorBusqAvanz import ControladorBusquedaAvanz


class MyApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('TravelFoodG7')
        self.geometry('600x500')
        self.resizable(False, False)
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)


    def inicializar(self):
        destinos = DestinoCulinario.cargar_de_json('data/destinos_culinarios.json')

        controlador_inicio = ControladorInicio(self)
        controlador_destinoCulinario = ControladorDestinoCulinario(self, destinos)
        controlador_info_destinos = ControladorInfo(self)
        controlador_mapa = ControladorMapa(self, destinos)
        controlador_calificacion = ControladorCalificacion(self)
        controlador_reviews = ControladorReview(self)
        #controladorBusquedaAvanz = ControladorBusquedaAvanz(self)
        controlador_busqueda = ControladorBusqueda(self, destinos)

        self.vista_inicio = VistaInicio(self, controlador_inicio)
        self.vista_destinoCulinario = VistaDestinosCulinarios(self, controlador_destinoCulinario)
        self.vista_info_destinos = VistaInfo(self, controlador_info_destinos)
        self.vista_calificacion = VistaCalificacion(self, controlador_calificacion)
        self.vista_review = VistaReview(self, controlador_reviews)
        self.vista_mapa = VistaMapa(self, controlador_mapa, controlador_mapa.seleccionar_ubicacion)
        self.vista_busqueda = VistaBusqueda(self, controlador_busqueda)


        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_destinoCulinario)
        self.ajustar_frame(self.vista_info_destinos)
        self.ajustar_frame(self.vista_calificacion)
        self.ajustar_frame(self.vista_review)
        self.ajustar_frame(self.vista_mapa)
        self.ajustar_frame(self.vista_busqueda)

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")

    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()

    def seleccionar_ubicacion(marcador):
        if marcador.image_hidden is True:
            marcador.hide_image(False)
        else:
            marcador.hide_image(True)
        print('Ubicacion seleccionada: ', marcador.text)


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
