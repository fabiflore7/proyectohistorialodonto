from .conexion import ConexionDB
from tkinter import messagebox

def listarHistoria(idPersona):
    conexion = ConexionDB()
    listarHistoria = []
    sql = '''SELECT h.idHistoria, p.apellido AS Apellidos, h.fechaHistoria, h.motivo, 
              h.Tratamiento, h.precioTratamiento, h.Estado 
              FROM historiaMedica h 
              INNER JOIN Persona p ON p.idPersona = h.idPersona 
              WHERE p.idPersona = ?'''
    try:
        conexion.cursor.execute(sql,(idPersona,))
        listarHistoria = conexion.cursor.fetchall()
    except Exception as e:
        title = 'LISTAR HISTORIA'
        mensaje = f'Error al listar Historia: {str(e)}'
        messagebox.showerror(title, mensaje)
    finally:
        conexion.cerrarConexion()
        
    return listarHistoria
    
    
def guardarHistoria(idPersona, fechaHistoria, motivo, Tratamiento, precioTratamiento, Estado):
    conexion = ConexionDB()
    sql = '''INSERT INTO historiaMedica (idPersona, fechaHistoria, motivo, Tratamiento, precioTratamiento, Estado)
             VALUES (?, ?, ?, ?, ?, ?)'''
    try:
        conexion.cursor.execute(sql, (idPersona, fechaHistoria, motivo, Tratamiento, precioTratamiento, Estado))
        conexion.commit()
        
        title = 'Registro Historia Odontologica'
        mensaje = 'Historia Registrada exitosamente'
        messagebox.showinfo(title, mensaje)
    except Exception as e:
        title = 'Registro Historia Odontologica'
        mensaje = f'Error al registrar historia: {str(e)}'
        messagebox.showerror(title, mensaje)
    finally:
        conexion.cerrarConexion()
        
def eliminarHistoria(idHistoria):
    conexion = ConexionDB()
    sql = f'DELETE FROM historiaMedica WHERE idHistoria = {idHistoria}'
    
    try:
        conexion.cursor.execute(sql)
        title = 'Eliminar Historia'
        mensaje = 'Historia Eliminada'
        messagebox.showinfo(title, mensaje)
    except Exception as e:
        title = 'Eliminar Historia'
        mensaje = f'Error al eliminar historia: {str(e)}'
        messagebox.showerror(title, mensaje)
    finally:
        conexion.cerrarConexion()    

def editarHistoria(fechaHistoria, motivo, Tratamiento, precioTratamiento, Estado, idHistoria):
    conexion = ConexionDB()
    sql = f"""UPDATE historiaMedica SET fechahistoria ='{fechaHistoria}',motivo='{motivo}',Tratamiento='{Tratamiento}',precioTratamiento='{precioTratamiento}',Estado='{Estado}' WHERE idHistoria = '{idHistoria}'"""
    try:
        conexion.cursor.execute(sql)
        title = 'EDITAR HISTORIA'
        mensaje = 'Los Cambios se han aplicado correctamente'
        messagebox.showinfo(title, mensaje)
    except Exception as e:
        title = 'EDITAR HISTORIA'
        mensaje = f'Error al EDITAR HISTORIA: {str(e)}'
        messagebox.showerror(title, mensaje)
    finally:
        conexion.cerrarConexion()
class historiaMedica:
    def __init__(self, idPersona, fechaHistoria, motivo, Tratamiento, precioTratamiento, Estado):
        
        self.idHistoria = None
        self.idPersona = idPersona
        self.fechaHistoria = fechaHistoria
        self.motivo = motivo
        self.Tratamiento = Tratamiento
        self.precioTratamiento = precioTratamiento
        self.Estado = Estado
        
    def __str__(self):
        return f'historiaMedica[{self.idPersona},{self.fechaHistoria},{self.motivo},{self.Tratamiento},{self.precioTratamiento},{self.Estado}]'
    