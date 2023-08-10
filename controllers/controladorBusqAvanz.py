class ControladorBusquedaAvanz:
    def __init__(self,app,mod_nombre, mod_tipo_cocina, mod_ingredientes, mod_precio_minimo,mod_precio_maximo,mod_popularidad,mod_disponibilidad, mod_id_ubicacion):
        self.app = app
        self.mod_nombre = mod_nombre
        self.mod_tipo_cocina= mod_tipo_cocina
        self.mod_ingredientes = mod_ingredientes
        self.mod_precio_minimo= mod_precio_minimo
        self.mod_precio_maximo =mod_precio_maximo
        self.mod_popularidad = mod_popularidad
        self.mod_disponibilidad = mod_disponibilidad
        self.mod_id_ubicacion = mod_id_ubicacion
        
    def obtener_nombre(self):
        return self.modelo_nombre , self.mod_tipo_cocina,self.mod_ingredientes,self.mod_precio_maximo,self.mod_precio_maximo,self.mod_popularidad,self.mod_disponibilidad,self.mod_id_ubicacion
    
    def seleccionar_nombre(self):
        indice = self.app.vista_busqueda.obtener_nombre_seleccionado()
        if indice is not None:
            busqueda= self.mod_nombre[indice]
            self.app.vista_info.mostrar_info_busqueda(busqueda)
            self.app.cambiar_frame(self.app.vista_info)
    
    def seleccionar_tipo_cocina(self):
        indice = self.app.vista_busqueda.obtener_tipo_cocina_seleccionado()
        if indice is not None:
            busqueda= self.mod_tipo_cocina[indice]
            self.app.vista_info.mostrar_info_busqueda(busqueda)
            self.app.cambiar_frame(self.app.vista_info)
            
    def seleccionar_ingredientes(self):
            indice = self.app.vista_busqueda.obtener_ingredientes_seleccionado()
            if indice is not None:
                busqueda= self.mod_ingredientes[indice]
                self.app.vista_info.mostrar_info_busqueda(busqueda)
                self.app.cambiar_frame(self.app.vista_info)
                
    def seleccionar_precio_minimo(self):
            indice = self.app.vista_busqueda.obtener_precio_minimo_seleccionado()
            if indice is not None:
                busqueda= self.mod_precio_minimo[indice]
                self.app.vista_info.mostrar_info_busqueda(busqueda)
                self.app.cambiar_frame(self.app.vista_info)
    
    def seleccionar_precio_maximo(self):
        indice = self.app.vista_busqueda.obtener_precio_maximo_seleccionado()
        if indice is not None:
            busqueda= self.mod_precio_maximo[indice]
            self.app.vista_info.mostrar_info_busqueda(busqueda)
            self.app.cambiar_frame(self.app.vista_info)

    def seleccionar_popularidad(self):
        indice = self.app.vista_busqueda.obtener_popularidad_seleccionado()
        if indice is not None:
            busqueda= self.mod_popularidad[indice]
            self.app.vista_info.mostrar_info_busqueda(busqueda)
            self.app.cambiar_frame(self.app.vista_info)      
            
    def seleccionar_disponibilidad(self):
        indice = self.app.vista_busqueda.obtener_disponibilidad_seleccionado()
        if indice is not None:
            busqueda= self.mod_disponibilidad[indice]
            self.app.vista_info.mostrar_info_busqueda(busqueda)
            self.app.cambiar_frame(self.app.vista_info)            
            
    def seleccionar_id_ubicacion(self):
        indice = self.app.vista_busqueda.obtener_id_ubicacion_seleccionado()
        if indice is not None:
            busqueda= self.mod_id_ubicacion[indice]
            self.app.vista_info.mostrar_info_busqueda(busqueda)
            self.app.cambiar_frame(self.app.vista_info)            
            
    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)
