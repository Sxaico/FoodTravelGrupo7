import tkinter as tk

class VistaBusqueda(tk.Frame):
    def __init__(self, app=None, controlador= None):
        super().__init__(app)
        self.app = app
        self.controlador = controlador
        
        self.lbl_resultados = tk.LabelFrame(self)
        self.lbl_resultados.grid()

        self.lbl_buscar = tk.LabelFrame(self)
        self.lbl_buscar.grid()

        self.lbl = tk.Label(self.lbl_buscar, text='Buscar')
        self.lbl.grid()

        self.lista = tk.Listbox(self.lbl_resultados)
        self.lista.grid()

        self.entrada = tk.Entry(self.lbl_buscar)
        self.entrada.grid()

        self.actualizar(self.destino_lista())

        self.lista.bind('<<ListboxSelect>>', self.fillout)
        self.entrada.bind('<KeyRelease>', self.checkeo)

        self.btn_volver = tk.Button(self.lbl_buscar, text='Volver a inicio', command=self.controlador.volver_inicio)
        self.btn_volver.grid()

    def destino_lista(self):
        self.destinos_lista = []
        self.destinos = self.controlador.obtener_destinos()
        #self.lista.delete(0, tk.END)
        for destino in self.destinos:
            #self.lista.insert(tk.END, destino.nombre)
            self.destinos_lista.append(destino.nombre)
        #for item in data:
        #    self.lista.insert(tk.END, item)
        return self.destinos_lista

    def actualizar(self,data):
        #self.destinos_lista = []
        #self.destinos = self.controlador.obtener_destinos()
        self.lista.delete(0, tk.END)
        #for destino in self.destinos:
            #self.lista.insert(tk.END, destino.nombre)
            #self.destinos_lista.append(destino.nombre)
        for item in data:
            self.lista.insert(tk.END, item)

    def fillout(self, e):
        self.entrada.delete(0, tk.END)
        self.entrada.insert(0, self.lista.get(self.lista.curselection()))
    
    def checkeo(self, e):
        tipeado = self.entrada.get()
        if tipeado == '':
            data = self.destinos_lista
        else:
            data = []
            for item in self.destinos_lista:
                if tipeado.lower() in item.lower():
                    data.append(item)
        self.actualizar(data)

            