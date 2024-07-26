import tkinter as tk
from tkinter import *
from tkinter import Button, ttk, scrolledtext, Toplevel
from tkinter import messagebox
from modelo.pacienteDao import Persona, guardarDatoPaciente, listar, listarCondicion
from modelo.pacienteDao import actualizarDatoPaciente,eliminarPaciente
import tkcalendar as tc
from tkcalendar import *
from tkcalendar import Calendar
from datetime import datetime, date

class Frame(tk.Frame):
    def __init__(self, root):

        super().__init__(root, width=1280, height=720)
        self.root = root
        self.pack()
        self.config(bg='#CDD8FF') 
        self.idPersona = None
        self.camposPacientes()
        self.deshabilitar()
        self.tablaPaciente()  # Asegúrate de que esto se llame después de inicializar listaPersona


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
        self.calendario = Toplevel()
        self.calendario.title('Fecha de Nacimiento ')
        self.calendario.resizable(0, 0)
        self.calendario.config(bg='#CDD8FF')
        
        
        self.svcalendario = StringVar(value='01-01-1990')
        self.calendar = tc.Calendar(self.calendario, selectmode = 'day', year = 1990, month=1
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
        
        self.btnHistorialPaciente = tk.Button(self, text = 'Historial Paciente')
        self.btnHistorialPaciente.config(width=20,font=('ARIAL',12,'bold'), fg = '#DAD5D6',bg='#007C79', activebackground='#99F2F0', cursor='sizing')
        self.btnHistorialPaciente.grid(column=2,row=12, padx=10, pady=5)
        
        self.btnSalir = tk.Button(self, text = 'Salir',command = self.root.destroy)
        self.btnSalir.config(width=20,font=('ARIAL',12,'bold'), fg = '#DAD5D6',bg='#000000', activebackground='#5E5E5E', cursor='sizing')
        self.btnSalir.grid(column=5,row=12, padx=10, pady=5)
        
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
            


