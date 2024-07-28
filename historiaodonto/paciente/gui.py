import tkinter as tk
from tkinter import *
from tkinter import Button, ttk, scrolledtext, Toplevel,LabelFrame
from tkinter import messagebox
from modelo.pacienteDao import Persona, guardarDatoPaciente, listar, listarCondicion
from modelo.pacienteDao import actualizarDatoPaciente,eliminarPaciente
import tkcalendar as tc
from tkcalendar import *
from tkcalendar import Calendar
from datetime import datetime, date
from modelo.historiamedicaDao import historiaMedica, guardarHistoria, listarHistoria,eliminarHistoria,editarHistoria

class Frame(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=1280, height=720)
        self.root = root
        self.pack()
        self.config(bg='#CDD8FF') 
        
        self.idPersona = None
        self.idPersonaHistoria = None
        self.idHistoria = None
        self.idHistoriaEditar = None
        
        self.camposPacientes()
        self.deshabilitar()
        self.tablaPaciente()  # Asegúrate de que esto se llame después de inicializar listaPersona
        
        self.svMotivoEditar = tk.StringVar()
        self.svTratamientoEditar = tk.StringVar()
        self.svprecioTratamientoEditar = tk.StringVar()
        self.svEstadoEditar = tk.StringVar()
        self.svfechaHistoriaEditar = tk.StringVar()

    def camposPacientes(self):

        #LABELS
        self.lblNombres = tk.Label(self, text='Nombre: ')
        self.lblNombres.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblNombres.grid(column=0, row=0, padx=10, pady=5)

        self.lblApellidos = tk.Label(self, text='Apellido: ')
        self.lblApellidos.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblApellidos.grid(column=0, row=1, padx=10, pady=5)

        self.lblCI = tk.Label(self, text='CI: ')
        self.lblCI.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblCI.grid(column=0, row=2, padx=10, pady=5)

        self.lblFechadeNacimiento = tk.Label(self, text='Fecha de nacimiento: ')
        self.lblFechadeNacimiento.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblFechadeNacimiento.grid(column=0, row=3, padx=10, pady=5)

        self.lblEdad = tk.Label(self, text='Edad: ')
        self.lblEdad.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblEdad.grid(column=0, row=4, padx=10, pady=5)

        self.lblAntecedentes = tk.Label(self, text='Antecedentes: ')
        self.lblAntecedentes.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblAntecedentes.grid(column=0, row=5, padx=10, pady=5)

        self.lblCorreo = tk.Label(self, text='Correo: ')
        self.lblCorreo.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblCorreo.grid(column=0, row=6, padx=10, pady=5)

        self.lblTelefono = tk.Label(self, text='Telefono: ')
        self.lblTelefono.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblTelefono.grid(column=0, row=7, padx=10, pady=5)

        #ENTRYS
        self.svNombres =  tk.StringVar()
        self.entryNombres = tk.Entry(self, textvariable=self.svNombres)
        self.entryNombres.config(width=50, font=('ARIAL' ,15))
        self.entryNombres.grid(column=1, row=0, padx=10, pady=5, columnspan=2)

        self.svApellidos =  tk.StringVar()
        self.entryApellidos = tk.Entry(self, textvariable=self.svApellidos)
        self.entryApellidos.config(width=50, font=('ARIAL' ,15))
        self.entryApellidos.grid(column=1, row=1, padx=10, pady=5, columnspan=2)

        self.svCI =  tk.StringVar()
        self.entryCI = tk.Entry(self, textvariable=self.svCI)
        self.entryCI.config(width=50, font=('ARIAL' ,15))
        self.entryCI.grid(column=1, row=2, padx=10, pady=5, columnspan=2)

        self.svFechadeNacimiento =  tk.StringVar()
        self.entryFechadeNacimiento = tk.Entry(self, textvariable=self.svFechadeNacimiento)
        self.entryFechadeNacimiento.config(width=50, font=('ARIAL' ,15))
        self.entryFechadeNacimiento.grid(column=1, row=3, padx=10, pady=5, columnspan=2)

        self.svEdad =  tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad)
        self.entryEdad.config(width=50, font=('ARIAL' ,15))
        self.entryEdad.grid(column=1, row=4, padx=10, pady=5, columnspan=2)

        self.svAntecedentes =  tk.StringVar()
        self.entryAntecedentes = tk.Entry(self, textvariable=self.svAntecedentes)
        self.entryAntecedentes.config(width=50, font=('ARIAL' ,15))
        self.entryAntecedentes.grid(column=1, row=5, padx=10, pady=5, columnspan=2)

        self.svCorreo =  tk.StringVar()
        self.entryCorreo = tk.Entry(self, textvariable=self.svCorreo)
        self.entryCorreo.config(width=50, font=('ARIAL' ,15))
        self.entryCorreo.grid(column=1, row=6, padx=10, pady=5, columnspan=2)

        self.svTelefono =  tk.StringVar()
        self.entryTelefono = tk.Entry(self, textvariable=self.svTelefono)
        self.entryTelefono.config(width=50, font=('ARIAL' ,15))
        self.entryTelefono.grid(column=1, row=7, padx=10, pady=5, columnspan=2)

        #BOTONES
        self.btnNuevo = tk.Button(self, text = 'Nuevo', command=self.habilitar)
        self.btnNuevo.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', 
                             bg='#1658A2', cursor='hand2',activebackground='#35BD6F')
        self.btnNuevo.grid(column=0,row=10, padx=5)

        self.btnGuardar = tk.Button(self, text='Guardar', command=self.guardarPaciente)
        self.btnGuardar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', 
                             bg='#000000', cursor='hand2',activebackground='#FDFA1D')
        self.btnGuardar.grid(column=1,row=10, padx=5)

        self.btnCancelar = tk.Button(self, text='Cancelar',command=self.deshabilitar)
        self.btnCancelar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', 
                             bg='#9E1C07', cursor='hand2',activebackground='#11FAF8')
        self.btnCancelar.grid(column=2,row=10, padx=5)
        
        #BUSCADOR
        #LABEL BUSCADOR
        self.lblBuscarCI = tk.Label(self, text ='Buscar por CI: ') 
        self.lblBuscarCI.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblBuscarCI.grid(column=4, row=0, padx=10, pady=5)
        
        #ENTRY BUSCADOR
        self.svBuscarCI =  tk.StringVar()
        self.entryBuscarCI = tk.Entry(self, textvariable=self.svBuscarCI)
        self.entryBuscarCI.config(width=20, font=('ARIAL' ,15))
        self.entryBuscarCI.grid(column=5, row=0, padx=10, pady=5, columnspan=2)
        
        #BUTTON BUSCADOR
        self.btnBuscador = tk.Button(self, text='Buscar', command=self.buscarCondicion)
        self.btnBuscador.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', 
                             bg='#0F279C', cursor='hand2',activebackground='#3454F2')
        self.btnBuscador.grid(column=4,row=1, padx=5)
        
        self.btnLimpiarBuscador = tk.Button(self, text='Limpiar', command=self.limpiarBuscador)
        self.btnLimpiarBuscador.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', 
                             bg='#891BC5', cursor='hand2',activebackground='#B149EA')
        self.btnLimpiarBuscador.grid(column=5,row=1, padx=5)
        #BUTTON CALENDARIO
        self.btnCalendario = tk.Button(self, text='Calendario', command=self.calendarView)
        self.btnCalendario.config(width=15, font=('ARIAL',12,'bold'), fg='#DAD5D6', 
                             bg='#3BCC0D', cursor='hand2',activebackground='#6CF141')
        self.btnCalendario.grid(column=4,row=3, padx=5)
    
    def calendarView(self):
        self.topcalendario = Toplevel()
        self.topcalendario.title('Fecha de Nacimiento ')
        self.topcalendario.resizable(0, 0)
        self.topcalendario.config(bg='#CDD8FF')
        
        
        self.svcalendario = StringVar(value='01-01-1990')
        self.calendar = tc.Calendar(self.topcalendario, selectmode = 'day', year = 1990, month=1
                                    , day=1, locate = 'es_US', bg='#777777', fg='#FFFFFF'
                                    , headersbackground='#B6DDFE', textvariable=self.svcalendario
                                    , cursor= 'hand2', date_pattern='dd-mm-Y')
        
        self.calendar.pack(pady=20)
        #TRACE ENVIAR FECHA
        self.svcalendario.trace('w', self.enviarFecha)
    
    def enviarFecha(self, *args):
        fecha_seleccionada = self.calendar.get_date()
        self.svFechadeNacimiento.set(fecha_seleccionada) # type: ignore
        if len(self.calendar.get_date()) > 1:
            self.svcalendario.trace('w', self.calcularEdad)
    
    def calcularEdad(self, *args): 
        self.fechaActual = date.today()
        self.date1 = self.calendar.get_date()
        self.conver = datetime.strptime(self.date1, "%d-%m-%Y")
        
        self.resul = self.fechaActual.year - self.conver.year
        self.resul -= ((self.fechaActual.month, self.fechaActual.day) 
                      < (self.conver.month, self.conver.day))
        self.svEdad.set(self.resul)
        
        
    
        
    def limpiarBuscador(self):
        self.svBuscarCI.set('')
        self.tablaPaciente()
    
    def buscarCondicion(self):
        if len(self.svBuscarCI.get()) > 0:
            where = "WHERE 1 = 1"
            if (len(self.svBuscarCI.get())) > 0:
                where = "WHERE CI = " + self.svBuscarCI.get() + "" #WHERE CI = 5660861
            self.tablaPaciente(where)  
        else:
            self.tablaPaciente()

    def guardarPaciente(self):
        persona = Persona(
        self.svNombres.get(), self.svApellidos.get(), self.svCI.get(),
        self.svFechadeNacimiento.get(), self.svEdad.get(), self.svAntecedentes.get(),
        self.svCorreo.get(), self.svTelefono.get()
        )
        if self.idPersona == None:
            # Aquí puedes llamar a una función para actualizar el registro en lugar de insertar uno nuevo
            guardarDatoPaciente(persona)
            
        else:
            actualizarDatoPaciente(self.idPersona, persona)
        
        self.deshabilitar()
        self.tablaPaciente()
        self.topcalendario.destroy()
        
    def habilitar(self):
        # habilita los campos de entrada y botones guardar y cancelar
        self.svNombres.set(""), self.svApellidos.set(""), self.svCI.set(""),
        self.svFechadeNacimiento.set(""), self.svEdad.set(""), self.svAntecedentes.set(""),
        self.svCorreo.set(""), self.svTelefono.set("")
        
        self.entryNombres.config(state='normal'), self.entryApellidos.config(state='normal'), self.entryCI.config(state='normal'),
        self.entryFechadeNacimiento.config(state='normal'), self.entryEdad.config(state='normal'), self.entryAntecedentes.config(state='normal'),
        self.entryCorreo.config(state='normal'), self.entryTelefono.config(state='normal')
        
        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')
        self.btnCalendario.config(state='normal')
    
    def deshabilitar(self):
        # deshabilitar los campos de entrada y botones guardar y cancelar
        self.idPersona = None
        self.svNombres.set(""), self.svApellidos.set(""), self.svCI.set(""),
        self.svFechadeNacimiento.set(""), self.svEdad.set(""), self.svAntecedentes.set(""),
        self.svCorreo.set(""), self.svTelefono.set("")
        
        self.entryNombres.config(state='disabled'), self.entryApellidos.config(state='disabled'), self.entryCI.config(state='disabled'),
        self.entryFechadeNacimiento.config(state='disabled'), self.entryEdad.config(state='disabled'), self.entryAntecedentes.config(state='disabled'),
        self.entryCorreo.config(state='disabled'), self.entryTelefono.config(state='disabled')
        
        self.btnGuardar.config(state='disabled')
        self.btnCancelar.config(state='disabled')
        self.btnCalendario.config(state='disabled')
        
    def tablaPaciente(self, where=""):
        
        if len(where) > 0:
            self.listaPersona = listarCondicion(where)
        else:
            self.listaPersona = listar()
        
        if self.listaPersona is None:  # Verifica si es None
            print("No se encontraron registros.")
            return
        
        
        self.tabla = ttk.Treeview(self, column=('Nombre', 'Apellido', 'CI', 'fechadenacimiento', 'edad', 'antecedentes', 'correo', 'telefono'))
        self.tabla.grid(column=0, row=11, columnspan=6, sticky='nsew')
        
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=11, column=5, sticky='nse')
        
        self.tabla.configure(yscrollcommand=self.scroll.set)
        
        self.tabla.tag_configure('evenrow', background='#C5EAFE')
        
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Apellido')
        self.tabla.heading('#3', text='CI')
        self.tabla.heading('#4', text='Fecha de nacimiento')
        self.tabla.heading('#5', text='Edad')
        self.tabla.heading('#6', text='Antecedentes')
        self.tabla.heading('#7', text='Correo')
        self.tabla.heading('#8', text='Telefono')
        
        self.tabla.column("#0", anchor=W, width=50)
        self.tabla.column("#1", anchor=W, width=150)
        self.tabla.column("#2", anchor=W, width=120)
        self.tabla.column("#3", anchor=W, width=80)
        self.tabla.column("#4", anchor=W, width=100)
        self.tabla.column("#5", anchor=W, width=50)
        self.tabla.column("#6", anchor=W, width=100)
        self.tabla.column("#7", anchor=W, width=150)
        self.tabla.column("#8", anchor=W, width=85)
        
        self.tabla.delete(*self.tabla.get_children())
        
        for p in self.listaPersona:           
            
            self.tabla.insert('', 0, text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8]), tags=('evenrow',))
        
        self.btnEditarPaciente = tk.Button(self, text = 'Editar Paciente',command=self.editarPaciente)
        self.btnEditarPaciente.config(width=20,font=('ARIAL',12,'bold'), fg = '#DAD5D6',bg='#170095', activebackground='#9379E0', cursor='exchange')
        self.btnEditarPaciente.grid(column=0,row=12, padx=10, pady=5)
        
        self.btnEliminarPaciente = tk.Button(self, text = 'Eliminar Paciente', command=self.eliminarDatosPaciente)
        self.btnEliminarPaciente.config(width=20,font=('ARIAL',12,'bold'), fg = '#DAD5D6',bg='#8A0000', activebackground='#D58A8A', cursor='pirate')
        self.btnEliminarPaciente.grid(column=1,row=12, padx=10, pady=5)
        
        self.btnHistorialPaciente = tk.Button(self, text = 'Historial Paciente',command=self.historialPaciente)
        self.btnHistorialPaciente.config(width=20,font=('ARIAL',12,'bold'), fg = '#DAD5D6',bg='#007C79', activebackground='#99F2F0', cursor='sizing')
        self.btnHistorialPaciente.grid(column=2,row=12, padx=10, pady=5)
        
        self.btnSalir = tk.Button(self, text = 'Salir',command = self.root.destroy)
        self.btnSalir.config(width=20,font=('ARIAL',12,'bold'), fg = '#DAD5D6',bg='#000000', activebackground='#5E5E5E', cursor='sizing')
        self.btnSalir.grid(column=5,row=12, padx=10, pady=5)
     
    def historialPaciente(self):
        
        try:
            if self.idPersona == None:
                self.idPersona = self.tabla.item(self.tabla.selection())['text']
                self.idPersonaHistoria = self.tabla.item(self.tabla.selection())['text']
            
            if (self.idPersona > 0):
                idPersona = self.idPersona
                
            self.tophistorialPaciente = Toplevel()
            self.tophistorialPaciente.title('Historial Odontologico')
            self.tophistorialPaciente.resizable(1,1)
            self.tophistorialPaciente.config(bg='#CDD8DF')
        
            self.listaHistoria = listarHistoria(idPersona)
            self.tablaHistoria = ttk.Treeview(self. tophistorialPaciente, columns=('Apellidos', 'fechaHistoria', 'motivo', 'Tratamiento', 'precioTratamiento', 'Estado') ) 
            self.tablaHistoria.grid(row=0, column=0, columnspan=8, sticky='nsew')
            
            self.scrollHistoria = ttk.Scrollbar(self.tophistorialPaciente, orient='vertical', command=self.tablaHistoria.yview)
            self.scrollHistoria.grid(row=0, column=8, columnspan=9, sticky='nsew')
            
            self.scrollxHistoria = ttk.Scrollbar(self.tophistorialPaciente, orient='horizontal', command=self.tablaHistoria.xview)
            self.scrollxHistoria.grid(row=1, column=0, columnspan=9, sticky='nsew')
            
            self.tablaHistoria.config(yscrollcommand=self.scrollHistoria.set)
            self.tablaHistoria.config(xscrollcommand=self.scrollxHistoria.set)
            
            self.tablaHistoria.heading('#0', text='ID')
            self.tablaHistoria.heading('#1', text='Apellidos')
            self.tablaHistoria.heading('#2', text='Fecha y Hora')
            self.tablaHistoria.heading('#3', text='Motivo')
            self.tablaHistoria.heading('#4', text='Tratamiento')
            self.tablaHistoria.heading('#5', text='Precio')
            self.tablaHistoria.heading('#6', text='Estado')
            
            self.tablaHistoria.column('#0', anchor=W, width=100)
            self.tablaHistoria.column('#1', anchor=W, width=200)
            self.tablaHistoria.column('#2', anchor=W, width=120)
            self.tablaHistoria.column('#3', anchor=W, width=200)
            self.tablaHistoria.column('#4', anchor=W, width=600)
            self.tablaHistoria.column('#5', anchor=W, width=100)
            self.tablaHistoria.column('#6', anchor=W, width=100)
            
            for p in self.listaHistoria:
                self.tablaHistoria.insert('',0, text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6]))

            self.btnGuardarHistoria=tk.Button(self.tophistorialPaciente, text = 'Agregar Historia', command=self.topAgregarHistoria)
            self.btnGuardarHistoria.config(width=20, font=('ARIAL', 12, 'bold'),fg='#DAD5D6', bg='#002771', cursor='hand2',activebackground='#7198E0')
            self.btnGuardarHistoria.grid(row=2,column=0, padx=10,pady=5)
            
            self.btnEditarHistoria=tk.Button(self.tophistorialPaciente, text = 'Editar Historia', command=self.topeditarHistoriaOdonto)
            self.btnEditarHistoria.config(width=20, font=('ARIAL', 12, 'bold'),fg='#DAD5D6', bg='#3A005D', cursor='hand2',activebackground='#B47CD6')
            self.btnEditarHistoria.grid(row=2,column=1, padx=10,pady=5)
            
            self.btnEliminarHistoria=tk.Button(self.tophistorialPaciente, text = 'Eliminar Historia',command=self.eliminarHistorialMedico)
            self.btnEliminarHistoria.config(width=20, font=('ARIAL', 12, 'bold'),fg='#DAD5D6', bg='#890011', cursor='hand2',activebackground='#DB939C')
            self.btnEliminarHistoria.grid(row=2,column=2, padx=10,pady=5)
            
            self.btnSalirHistoria=tk.Button(self.tophistorialPaciente, text = 'Salir', command=self.tophistorialPaciente.destroy)
            self.btnSalirHistoria.config(width=20, font=('ARIAL', 12, 'bold'),fg='#DAD5D6', bg='#000000', cursor='hand2',activebackground='#6F6F6F')
            self.btnSalirHistoria.grid(row=2,column=7, padx=10,pady=5)
        
        except Exception as e:
            title = 'Historia Odontologica'
            mensaje = f'Error al mostrar historial: {str(e)}'
            messagebox.showerror(title, mensaje)
        
    def topAgregarHistoria(self):  
        self.topAHistoria = Toplevel()
        self.topAHistoria.title('AGREGAR HISTORIA')
        self.topAHistoria.resizable(0,0)
        self.topAHistoria.config(bg='#CDD8FF')
        
        ##FRAME1
        
        self.frameDatosHistoria = tk.LabelFrame(self.topAHistoria, text='Datos de Historia', bg='#CDD8FF')
        self.frameDatosHistoria.pack(fill="both", expand="yes", pady=10, padx=20)
        
        #labels agregar historia medica
        self.lblmotivoHistoria = tk.Label(self.frameDatosHistoria, text='Motivo de la Historia Odontologica', width=30,font=('ARIAL',12), bg='#CDD8FF')
        self.lblmotivoHistoria.grid(row=0, column=1, padx=5, pady=3)
        
        self.lbltratamientoHistoria = tk.Label(self.frameDatosHistoria, text='Tratamiento', width=30,font=('ARIAL',12), bg='#CDD8FF')
        self.lbltratamientoHistoria.grid(row=2, column=1, padx=5, pady=3)
        
        self.lblpreciotratamiento = tk.Label(self.frameDatosHistoria, text='Precio', width=20,font=('ARIAL',12), bg='#CDD8FF')
        self.lblpreciotratamiento.grid(row=4, column=1, padx=5, pady=3)
        
        self.lblestadoTratamiento = tk.Label(self.frameDatosHistoria, text='Estado', width=20,font=('ARIAL',12), bg='#CDD8FF')
        self.lblestadoTratamiento.grid(row=6, column=1, padx=5, pady=3)
        
        #ENTRY AGREGAR HISTORIA
        self.svmotivoHistoria = tk.StringVar()
        self.MotivoHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svmotivoHistoria)
        self.MotivoHistoria.config( width = 70, font=('ARIAL', 11))
        self.MotivoHistoria.grid(row= 1, column=0, pady=3, padx=5, columnspan=3)
        
        #ENTRY AGREGAR HISTORIA
        self.svtratamientoHistoria = tk.StringVar()
        self.TRATAMIENTOHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svtratamientoHistoria)
        self.TRATAMIENTOHistoria.config( width = 70, font=('ARIAL', 11))
        self.TRATAMIENTOHistoria.grid(row= 3, column=0, pady=3, padx=5, columnspan=3)
        
        #ENTRY AGREGAR HISTORIA
        self.svpreciotratamiento = tk.StringVar()
        self.PRECIOTratamiento = tk.Entry(self.frameDatosHistoria, textvariable=self.svpreciotratamiento)
        self.PRECIOTratamiento.config( width = 70, font=('ARIAL', 11))
        self.PRECIOTratamiento.grid(row= 5, column=0, pady=3, padx=5, columnspan=3)
        
        #ENTRY AGREGAR HISTORIA
        self.svestadoTratamiento = tk.StringVar()
        self.ESTADOTratamiento = tk.Entry(self.frameDatosHistoria, textvariable=self.svestadoTratamiento)
        self.ESTADOTratamiento.config( width = 70, font=('ARIAL', 11))
        self.ESTADOTratamiento.grid(row= 7, column=0, pady=3, padx=5, columnspan=3)
        #FRAME2
        self.frameFechaHistoria = tk.LabelFrame(self.topAHistoria, text='Fecha y Hora', bg='#CDD8FF')
        self.frameFechaHistoria.pack(fill="both", expand="yes", pady=20, padx=10)
        
        #LABEL FECHA AGREGAR HISTORIA
        
        self.lblFechahistoria = tk.Label(self.frameFechaHistoria, text='Fecha y Hora', width=20, font=('ARIAL',12), bg='#ADBDF7')
        self.lblFechahistoria.grid(row=1, column=0, padx=5, pady=3)
        
        #ENTRY FECHA AGREGAR HISTORIa
        
        self.svFechahistoria = tk.StringVar()
        self.entryFECHAhistoria = tk.Entry(self.frameFechaHistoria, textvariable=self.svFechahistoria, width=25, font=('ARIAL', 12))
        self.entryFECHAhistoria.grid(row=1, column=0, pady=3, padx=5)
        
        #TRAER FECHA Y HORA ACTUAL
        self.svFechahistoria.set(datetime.today().strftime('%d-%m-%Y %H:%M '))
        
        #BUTTONS
        self.btnAgregarHistoria = tk.Button(self.frameFechaHistoria, text = 'Agregar Historia', command=self.agregarHistoriaMedica)
        self.btnAgregarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000992', cursor='hand2',activebackground='#4E56C6')
        self.btnAgregarHistoria.grid(row=2,column=0, padx=10,pady=5)
        
        self.btnSALIRAGREGARhistoria = tk.Button(self.frameFechaHistoria, text = 'Salir', command=self.topAHistoria.destroy)
        self.btnSALIRAGREGARhistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000000', cursor='hand2',activebackground='#646464')
        self.btnSALIRAGREGARhistoria.grid(row=2,column=1, padx=10,pady=5)
        
    def agregarHistoriaMedica(self):
        try:
            if self.idHistoria == None:
                guardarHistoria(self.idPersonaHistoria, self.svFechahistoria.get(),self.svmotivoHistoria.get(),self.svtratamientoHistoria.get(),self.svpreciotratamiento.get(),self.svestadoTratamiento.get())
            self.topAHistoria.destroy()
            self.tophistorialPaciente.destroy()
        except Exception as e:
            title = 'Agregar historia'
            mensaje = f'Error al Agregar historial: {str(e)}'
            messagebox.showerror(title, mensaje)
    
    def eliminarHistorialMedico(self):
        try:
            self.idHistoria = self.tablaHistoria.item(self.tablaHistoria.selection())['text']
            eliminarHistoria(self.idHistoria)
            
            self.idHistoria = None
            self.tophistorialPaciente.destroy()
        except Exception as e:
            title = 'Eliminar Historia'
            mensaje = f'Error al Eliminar historia1: {str(e)}'
            messagebox.showerror(title, mensaje)
    def topeditarHistoriaOdonto(self): # type: ignore
        try:
            selected_item = self.tablaHistoria.selection()
            if not selected_item:
                messagebox.showwarning("Advertencia", "Por favor, selecciona una historia para editar.")
                return

            item = self.tablaHistoria.item(selected_item)
            if len(item['values']) < 6:
                messagebox.showwarning("Advertencia", "La historia seleccionada no contiene suficientes datos.")
                return
            
             # Asignar valores a las variables de texto antes de abrir la ventana
            self.idHistoriaEditar = item['text']
            self.fechaHistoriaEditar = item['values'][1]
            self.motivoHistoriaEditar = item['values'][2]
            self.TratamientoHistoriaEditar = item['values'][3]
            self.precioTratamientoHistoriaEditar = item['values'][4]
            self.EstadoHistoriaEditar = item['values'][5]

            # Asignar valores a las variables de texto
            self.svfechaHistoriaEditar.set(datetime.today().strftime('%d-%m-%Y   %H:%M '))
            self.svMotivoEditar.set(self.motivoHistoriaEditar)
            self.svTratamientoEditar.set(self.TratamientoHistoriaEditar)
            self.svprecioTratamientoEditar.set(self.precioTratamientoHistoriaEditar)
            self.svEstadoEditar.set(self.EstadoHistoriaEditar)
            

            self.topEditarHistoria = Toplevel()
            self.topEditarHistoria.title('Editar HISTORIA MEDICA')
            self.topEditarHistoria.resizable(0, 0)
            self.topEditarHistoria.config(bg='#CDD8FF')
            
            #FRAME EDITAR DATOS HISTORIA
            self.frameEditarDatos = tk.LabelFrame(self.topEditarHistoria, text='Editar Datos', bg='#CDD8FF', font=('ARIAL', 12, 'bold'))
            self.frameEditarDatos.pack(fill="both", expand="yes", padx=20,pady=10)
            
            #LABEL EDITAR HISTORIA
            self.lblMotivoEditar = tk.Label(self.frameEditarDatos, text= 'Motivo de la historia:', width = 30, font= ('ARIAL', 12 ), bg= '#CDD8FF')
            self.lblMotivoEditar.grid(row=0, column=0, padx=5, pady=5, sticky='w')
            
            self.lblTratamientoEditar = tk.Label(self.frameEditarDatos, text= 'Tratamiento:', width = 30, font= ('ARIAL', 12 ), bg= '#CDD8FF')
            self.lblTratamientoEditar.grid(row=1, column=0, padx=5, pady=5, sticky='w')
            
            self.lblprecioTratamientoEditar = tk.Label(self.frameEditarDatos, text= 'Precio:', width = 30, font= ('ARIAL', 12 ), bg= '#CDD8FF')
            self.lblprecioTratamientoEditar.grid(row=2, column=0, padx=5, pady=5, sticky='w')
            
            self.lblEstadoEditar = tk.Label(self.frameEditarDatos, text= 'Estado:', width = 30, font= ('ARIAL', 12 ), bg= '#CDD8FF')
            self.lblEstadoEditar.grid(row=3, column=0, padx=5, pady=5, sticky='w')
            
            #ENTRYS EDITAR HISTORIA
            
            self.svMotivoEditar = tk.StringVar()
            self.MOtivoEditar  = tk.Entry(self.frameEditarDatos, textvariable=self.svMotivoEditar, width=70, font=('ARIAL', 11))
            self.MOtivoEditar .grid(row=0, column=1, pady=5, padx=5)
        
            self.svTratamientoEditar = tk.StringVar()
            self.TRatamientoEditar = tk.Entry(self.frameEditarDatos, textvariable=self.svTratamientoEditar, width=70, font=('ARIAL', 11))
            self.TRatamientoEditar.grid(row=1, column=1, pady=5, padx=5)

            self.svprecioTratamientoEditar = tk.StringVar()
            self.precioTratamientoEditar = tk.Entry(self.frameEditarDatos, textvariable=self.svprecioTratamientoEditar, width=70, font=('ARIAL', 11))
            self.precioTratamientoEditar.grid(row=2, column=1, pady=5, padx=5)

            self.svEstadoEditar = tk.StringVar()
            self.EStadoEditar = tk.Entry(self.frameEditarDatos, textvariable=self.svEstadoEditar, width=70, font=('ARIAL', 11))
            self.EStadoEditar.grid(row=3, column=1, pady=5, padx=5)
            
            
            #FRAME FECHA EDITAR

            self.frameFechaEditar = tk.LabelFrame(self.topEditarHistoria, text='Fecha y Hora', bg='#CDD8FF')
            self.frameFechaEditar.pack(fill="both", expand="yes", padx=5, pady=5)

            #LABEL FECHA EDITAR
            
            self.lblfechaHistoriaEditar = tk.Label(self.frameFechaEditar, text= 'Fecha y Hora:', width = 30, font= ('ARIAL', 12 ), bg= '#CDD8FF')
            self.lblfechaHistoriaEditar.grid(row=0, column=0, padx=5, pady=3, sticky='w')
            
            #ENTRY FECHA EDITAR
            
            self.svfechaHistoriaEditar = tk.StringVar()
            self.FEchaHistoriaEditar = tk.Entry(self.frameFechaEditar, textvariable=self.svfechaHistoriaEditar, width=20, font=('ARIAL', 11))
            self.FEchaHistoriaEditar.grid(row=1, column=0, pady=5, padx=5)
            
            #Elimina la fecha anterior y establece la fecha actual
            self.svfechaHistoriaEditar.set(datetime.today().strftime('%d-%m-%Y   %H:%M '))
            
            #INSERTAR VALORES A ENTRYS
            
            self.MOtivoEditar.insert(0, self.motivoHistoriaEditar)
            self.TRatamientoEditar.insert(0, self.TratamientoHistoriaEditar)
            self.precioTratamientoEditar.insert(0, self.precioTratamientoHistoriaEditar)
            self.EStadoEditar.insert(0, self.EstadoHistoriaEditar)
            
            
        
            # BUTTONS
            self.btnFrame = tk.Frame(self.topEditarHistoria, bg='#CDD8FF')  # Frame para centrar botones
            self.btnFrame.pack(pady=10)

            self.btnsobreeditarHistoria = tk.Button(self.btnFrame, text='Actualizar Historia', width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000992', cursor='hand2', activebackground='#4E56C6',command=self.actualizar_historia)
            self.btnsobreeditarHistoria.grid(row=0, column=0, padx=10)

            self.btnSALIREditarhistoria = tk.Button(self.btnFrame, text='Salir', command=self.topEditarHistoria.destroy, width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000000', cursor='hand2', activebackground='#646464')
            self.btnSALIREditarhistoria.grid(row=0, column=1, padx=10)

            if self.idHistoriaEditar == None:
                self.idHistoriaEditar = self.idHistoria
            self.idHistoria = None

        except Exception as e:
            messagebox.showerror("Editar Historia", f"Error al editar Historia: {e}")
    
    def actualizar_historia(self):
        # Verificar si los campos están vacíos
        if not self.svMotivoEditar.get() or not self.svTratamientoEditar.get() or not self.svprecioTratamientoEditar.get() or not self.svEstadoEditar.get():
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        try:
            # Obtener los valores de los Entry
            nueva_fecha = self.svfechaHistoriaEditar.get()
            nuevo_motivo = self.svMotivoEditar.get()
            nuevo_tratamiento = self.svTratamientoEditar.get()
            nuevo_precio = self.svprecioTratamientoEditar.get()
            nuevo_estado = self.svEstadoEditar.get()
            

            # Solo actualizar si los valores han cambiado
            if (nueva_fecha != self.fechaHistoriaEditar or
                nuevo_motivo != self.motivoHistoriaEditar or
                nuevo_tratamiento != self.TratamientoHistoriaEditar or
                nuevo_precio != self.precioTratamientoHistoriaEditar or
                nuevo_estado != self.EstadoHistoriaEditar):

                editarHistoria(nueva_fecha, nuevo_motivo, nuevo_tratamiento, nuevo_precio, nuevo_estado, self.idHistoriaEditar)

            # Limpiar las variables de ID
            self.idHistoriaEditar = None
            self.idHistoria = None

            self.topEditarHistoria.destroy()
            self.tophistorialPaciente.destroy()
        except Exception as e:
            messagebox.showerror("Actualizar Historia", f"Error al Actualizar Historia: {e}")
            self.topEditarHistoria.destroy()
    
    def editarPaciente(self):
        try:
            selected_item = self.tabla.selection()
            if not selected_item:
                messagebox.showwarning("Editar Paciente", "Por favor, selecciona un paciente para editar.")
                return

            self.idPersona = self.tabla.item(selected_item)['text']  # Trae el id
            values = self.tabla.item(selected_item)['values']  # Obtiene los valores

            # Asegúrate de que 'values' contenga los datos esperados
            if len(values) < 8:
                messagebox.showwarning("Editar Paciente", "Error al obtener los datos del paciente.")
                return

            self.nombrePaciente = values[0]
            self.apellidoPaciente = values[1]
            self.CIPaciente = values[2]
            self.fechadenacimientoPaciente = values[3]
            self.edadPaciente = values[4]
            self.antecedentesPaciente = values[5]
            self.correoPaciente = values[6]
            self.telefonoPaciente = values[7]

            self.habilitar()

            # Rellena los campos de entrada con los datos del paciente
            self.entryNombres.delete(0, tk.END)
            self.entryNombres.insert(0, self.nombrePaciente)

            self.entryApellidos.delete(0, tk.END)
            self.entryApellidos.insert(0, self.apellidoPaciente)

            self.entryCI.delete(0, tk.END)
            self.entryCI.insert(0, self.CIPaciente)

            self.entryFechadeNacimiento.delete(0, tk.END)
            self.entryFechadeNacimiento.insert(0, self.fechadenacimientoPaciente)

            self.entryEdad.delete(0, tk.END)
            self.entryEdad.insert(0, self.edadPaciente)

            self.entryAntecedentes.delete(0, tk.END)
            self.entryAntecedentes.insert(0, self.antecedentesPaciente)

            self.entryCorreo.delete(0, tk.END)
            self.entryCorreo.insert(0, self.correoPaciente)

            self.entryTelefono.delete(0, tk.END)
            self.entryTelefono.insert(0, self.telefonoPaciente)

        except Exception as e:
            messagebox.showerror("Editar Paciente", f"Error al editar paciente: {e}")
    
    def eliminarDatosPaciente(self):
        
        try:
            selected_item = self.tabla.selection()
            if not selected_item:
                messagebox.showwarning("Eliminar Paciente", "Por favor, selecciona un paciente para eliminar.")
                return

            self.idPersona = self.tabla.item(selected_item)['text']  # Trae el id
            eliminarPaciente(self.idPersona)       
        
        except Exception as e:
            messagebox.showerror("Eliminar Paciente", f"Error al eliminar paciente: {e}")
        
        self.deshabilitar()
        self.tablaPaciente()    
            


