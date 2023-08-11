from models.ubicacion import Ubicacion
from PIL import Image, ImageTk

class ControladorMapa:
    def __init__(self, app, destinos):
        self.app = app
        self.destinos = destinos
        self.ubicaciones = Ubicacion.cargar_de_json('data/ubicaciones.json')
        self.marcadores = []
        self.imagenes = []

        self.cargar_imagenes()
        #self.cargar_marcadores()


    def cargar_imagenes(self):
        for destino in self.destinos:
            imagen = ImageTk.PhotoImage(Image.open(f'assets/images/{destino.imagen}').resize((100,100)))
            self.imagenes.append(imagen)

    #def cargar_marcadores(self):
        #for ubicacion, destino in zip(self.ubicaciones, self.destinos):
            #imagen = self.imagenes[ubicacion.id-1]
            #marcador = self.app.agregar_marcador_mapa(ubicacion.coordenadas[0], ubicacion.coordenadas[1], destino.nombre, imagen)
            #marcador.hide_image(True)
            #self.marcadores.append(marcador)
    
    def obtener_destinos(self):
        return self.destinos

    def seleccionar_destino(self):
        indice = self.app.vista_mapa.obtener_indice()
        destino_seleccionado = self.destinos[indice]
        ubicacion_seleccionada = Ubicacion(0,'',[0,0])

        for ubicacion in self.ubicaciones:
            if ubicacion.id == destino_seleccionado.id_ubicacion:
                ubicacion_seleccionada = ubicacion
                break
        self.app.vista_mapa.mapa.set_position(ubicacion_seleccionada.coordenadas[0], ubicacion_seleccionada.coordenadas[1])

    def seleccionar_ubicacion(marcador):
        if marcador.image_hidden is True:
            marcador.hide_image(False)
        else:
            marcador.hide_image(True)
        print("Ubicación seleccionada: ", marcador.text)

    def volver_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)