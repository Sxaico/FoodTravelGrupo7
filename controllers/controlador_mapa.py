from views.vista_mapa import VistaPrincipalMapa
from models.destinoCulinario import DestinoCulinario
from models.ubicacion import Ubicacion
from PIL import Image, ImageTk


class ControladorMapa:
    def __init__(self, app):
        self.app = app
        self.vista = VistaPrincipalMapa(app, self.seleccionar_destino, seleccionar_ubicacion) 
        self.destino = DestinoCulinario.cargar_de_json('data/destinos_culinarios.json')
        self.ubicacion = Ubicacion.cargar_de_json('data/ubicaciones.json')

        self.marcadores = []
        self.imagenes = []

        self.cargar_destinos()
        self.cargar_imagenes()
        self.cargar_marcadores()

    def cargar_destinos(self):
        for destino in self.destino:
            self.vista.agregar_destino(destino)

    def cargar_imagenes(self):
        for destino in self.destino:
            imagen = ImageTk.PhotoImage(Image.open(f'assets/images/{destino.imagen}').resize((200,200)))
            self.imagenes.append(imagen)

    def cargar_marcadores(self):
        for ubicacion, destino in zip(self.ubicacion, self.destino):
            print(f'{ubicacion.id},{destino.nombre}, {ubicacion.coordenadas[0]}, {ubicacion.coordenadas[1]}')
            imagen = self.imagenes[ubicacion.id - 1]
            marcador = self.vista.agregar_marcador_mapa(ubicacion.coordenadas[0], ubicacion.coordenadas[1], destino.nombre, imagen)
            marcador.hide_image(True)
            self.marcadores.append(marcador)
            #print(f'{self.marcadores[ubicacion.id-1]}')

    def seleccionar_destino(self, event):
        indice_seleccionado = self.vista.lista_destinos.curselection()
        destino_seleccionado = self.destino[indice_seleccionado[0]]

        ubicacion_seleccionada = Ubicacion(0,'',[0,0])

        for ubicacion in self.ubicacion:
            if ubicacion.id == destino_seleccionado.id_ubicacion:
                ubicacion_seleccionada = ubicacion
                break

        self.vista.mapa.set_position(ubicacion_seleccionada.coordenadas[0], ubicacion_seleccionada.coordenadas[1])

        print(f'Latitud: {ubicacion_seleccionada.coordenadas[0]}, Longitud: {ubicacion_seleccionada.coordenadas[1]}')


def seleccionar_ubicacion(marcador):
    if marcador.image_hidden is True:
        marcador.hide_image(False)
    else:
        marcador.hide_image(True)
    print('Ubicacion seleccionada: ', marcador.text)
