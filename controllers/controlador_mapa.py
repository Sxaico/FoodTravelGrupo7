from views.vista_mapa import VistaPrincipalMapa
from models.destinoCulinario import DestinoCulinario
from models.ubicacion import Ubicacion
from PIL import Image, ImageTk


class ControladorMapa:
    def __init__(self, app):
        self.vista = VistaPrincipalMapa(app, self.seleccionar_destino, self.seleccionar_ubicacion)
        self.destino = DestinoCulinario.cargar_de_json('data/destinos_culinarios.json')
        self.ubicaciones = Ubicacion.cargar_de_json('data/ubicaciones.json')
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
        '''
        for ubicacion in self.ubicaciones:
            print(f'{ubicacion.id}')
            '''
        for ubicacion, destino in zip(self.ubicaciones, self.destino):
            print(f'{ubicacion.id -1 }')
            imagen = self.imagenes[ubicacion.id - 1]
            marcador = self.vista.agregar_marcador_mapa(ubicacion.coordenadas[0], ubicacion.coordenadas[1], destino.nombre, imagen)
            marcador.hide_image(True)
            self.marcadores.append(marcador)

    def seleccionar_destino(self, event):
        # Obtenemos el indice del evento seleccionado
        indice_seleccionado = self.vista.lista_destinos.curselection()
        # Obtenemos el destino seleccionado
        destino_seleccionado = self.destino[indice_seleccionado[0]]

        ubicacion_seleccionada = Ubicacion(0, 0, 0, '')

        # Busca la ubicación correspondiente al destino seleccionado
        for ubicacion in self.ubicaciones:
            if ubicacion.id == destino_seleccionado.id_ubicacion:
                ubicacion_seleccionada = ubicacion
                break

        # Centramos el mapa en la ubicación seleccionada
        self.vista.mapa.set_position(ubicacion_seleccionada.coordenadas[0], ubicacion_seleccionada.coordenadas[1])

        print(f'Latitud: {ubicacion_seleccionada.coordenadas[0]}, Longitud: {ubicacion_seleccionada.coordenadas[1]}')

    def seleccionar_ubicacion(marcador):
        if marcador.imagen_idden is True:
            marcador.hide_image(False)
        else:
            marcador.hide_image(True)
        print('Ubicación seleccioada: ', marcador.text)

    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)
