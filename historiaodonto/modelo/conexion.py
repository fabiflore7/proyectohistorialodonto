import sqlite3

class ConexionDB:
    def __init__(self):
        self.baseDatos = 'database/dbhistorialodonto.db'
        self.conexion = sqlite3.connect(self.baseDatos)
        self.cursor = self.conexion.cursor()
        
    def commit(self):
        self.conexion.commit()
    
    def cerrarConexion(self):
        self.conexion.commit()
        self.conexion.close()
        