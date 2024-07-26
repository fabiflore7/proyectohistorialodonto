from .conexion import ConexionDB
from tkinter import messagebox

def guardarDatoPaciente(persona):
    conexion = ConexionDB()
    sql = f"""INSERT INTO Persona (nombre, apellido, CI, fechadenacimiento, edad, antecedentes, correo, telefono, activo) 
                VALUES('{persona.nombre}', '{persona.apellido}', '{persona.CI}', '{persona.fechadenacimiento}', '{persona.edad}', '{persona.antecedentes}'
                , '{persona.correo}', '{persona.telefono}',1)"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registrar Paciente'
        mensaje = 'Paciente Registrado Exitosamente'
        messagebox.showinfo(title, mensaje)
        
    except:
        title = 'Registrar Paciente'
        mensaje = 'Error al registrar paciente'
        messagebox.showinfo(title, mensaje)

def listar():
    conexion = ConexionDB()
    listaPersona = []
    sql = 'SELECT * FROM Persona WHERE activo = 1'
    
    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'Registros no existen'
        messagebox.showwarning(title, mensaje)  
    return listaPersona  # Asegúrate de devolver la lista       

def listarCondicion(where):
    conexion = ConexionDB()
    listaPersona =  []
    sql = f'SELECT * FROM Persona {where}'
    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
    except:
        title = 'Datos'
        mensaje = 'Registros no existen'
        messagebox.showwarning(title, mensaje)
    return listaPersona  # Asegúrate de devolver la lista

def actualizarDatoPaciente(idPersona, persona):
    conexion = ConexionDB()
    sql = f"""UPDATE Persona SET 
                nombre = '{persona.nombre}', 
                apellido = '{persona.apellido}', 
                CI = '{persona.CI}', 
                fechadenacimiento = '{persona.fechadenacimiento}', 
                edad = '{persona.edad}', 
                antecedentes = '{persona.antecedentes}', 
                correo = '{persona.correo}', 
                telefono = '{persona.telefono}', 
                activo = 1
                WHERE idPersona = {idPersona}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        messagebox.showinfo("Actualizar Paciente", "Paciente actualizado exitosamente.")
    except Exception as e:
        messagebox.showerror("Actualizar Paciente", f"Error al actualizar paciente: {e}")
    

def eliminarPaciente(idPersona):
        conexion = ConexionDB()
        sql = f"""UPDATE Persona SET activo = 0 WHERE idPersona = {idPersona}"""
        try:
            conexion.cursor.execute(sql)
            conexion.cerrarConexion()
            title = 'Eliminar Paciente'
            mensaje = 'Paciente eliminado exitosamente'
            messagebox.showwarning(title, mensaje)
        except:
            title = 'Eliminar Paciente'
            mensaje = 'Error al eliminar Paciente'
            messagebox.showwarning(title, mensaje)
        
class Persona:
    def __init__(self, nombre, apellido, CI, fechadenacimiento, edad, antecedentes, correo, telefono ):
        self.idPersona = None
        self.nombre = nombre
        self.apellido = apellido
        self.CI = CI
        self.fechadenacimiento = fechadenacimiento
        self.edad = edad
        self.antecedentes = antecedentes
        self.correo = correo
        self.telefono = telefono
        
    
    def __str__(self):
        return f'Persona[{self.nombre},{self.apellido},{self.CI},{self.fechadenacimiento},{self.edad},{self.antecedentes},{self.correo},{self.telefono}]'
        
        

