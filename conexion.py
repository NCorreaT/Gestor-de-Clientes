
import sqlite3

class Cliente:

    def abrir(self):
        conexion = sqlite3.connect('clientes.db')
        cursor = conexion.cursor()

        cursor.execute("""   
        CREATE TABLE if not exists cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            email TEXT NOT NULL,
            empresa TEXT NOT NULL
            );
        """)
        conexion.commit()
        return conexion
    
    def cargar_datos(self):#Cargar lista de clientes
        conexion = self.abrir()
        cursor = conexion.cursor()
        rows = cursor.execute("SELECT * FROM cliente").fetchall()
        return rows

    def cargar_datos_top(self, id):#Cargar datos del cliente que se selecciono
        conexion = self.abrir()
        cursor = conexion.cursor()
        rows = cursor.execute("SELECT * FROM cliente WHERE id = ?",(id, )).fetchone()
        return rows

    def insertar_datos(self, cliente):#Ingresar nuevo cliente
        conexion = self.abrir()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO cliente (nombre, telefono,email, empresa) values (?, ?, ?, ?)
            """, (cliente['nombre'], cliente['telefono'], cliente['email'], cliente['empresa']))
        conexion.commit()

    def modificar_datos(self, cliente,id):#Modificar datos 
        conexion = self.abrir()
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE cliente SET nombre = ?, telefono = ?,email = ?, empresa = ? WHERE id = ?
            """, (cliente['nombre'], cliente['telefono'], cliente['email'], cliente['empresa'],id)).fetchone()
        conexion.commit()

    def buscar_cliente(self, id):#Buscar al cliente que se selecciona
        conexion = self.abrir()
        cursor = conexion.cursor()
        rows = cursor.execute("SELECT * FROM cliente WHERE id = ?",(id, )).fetchone()
        return rows

    def eliminar(self,id):#Eliminar cliente
        conexion = self.abrir()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM cliente WHERE id = ?",(id, ))
        conexion.commit()

        
