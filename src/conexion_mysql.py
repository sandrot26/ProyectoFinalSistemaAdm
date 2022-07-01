from sqlite3 import Cursor
import mysql.connector
from mysql.connector import Error

class DAO:

#Conexion a base de datos
    def __init__(self):

        try:
            connection=mysql.connector.connect(
            host="localHost",
            port=3306,
            user="root",
            password="754200",
            db="sistemaadm"
        )

            if connection.is_connected():
                print("conexion exitosa")
                info_server=connection.get_server_info()
                print(info_server)
                cursor=connection.cursor()
                cursor.execute("SELECT DATABASE()")
                row=cursor.fetchone()
                print("conectado a la base de datos: {}".format(row))

        except Error as ex:
            print("Error al intentar conexion: {0}".format(ex))

#Ver lista de productos
    def listarProducts(self):
        
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM products ORDEN BY nameProduct ASC")
                resultados = cursor.fetchall()
                return resultados

            except Error as ex:
                print("Error al intentar conexion: {0}".format(ex))
    

#Ver lista de Clientes
    def listarClients(self):
        
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM clients ORDEN BY name ASC")
                resultados = cursor.fetchall()
                return resultados

            except Error as ex:
                print("Error al intentar conexion: {0}".format(ex))

#Ver lista de Empleados
    def listarEmployees(self):
        
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM employees ORDEN BY nameEmployees ASC")
                resultados = cursor.fetchall()
                return resultados

            except Error as ex:
                print("Error al intentar conexion: {0}".format(ex))
    
#Agregar nuevo cliente Base de datos
    def nuevoCliente(self, clients):
          if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO clients (names, surnames, dni, direction, phone, email) VALUES ('{0}','{1}','{2}', '{3}','{4}','{5}')"
                cursor.execute(sql.format(clients[0], clients[1], clients[2], clients[3], clients[4], clients[5]))
                self.conexion.commit()
                print("Se cargo correctamente el cliente\n")

            except Error as ex:
                print("Error al intentar conexion: {0}".format(ex))

#Agregar nuevo empleado Base de datos
    def nuevoEmpleado(self, employees):
          if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO employees (namesEmployee, surnameEmployee, dniEmployee, phoneEmployee) VALUES ('{0}','{1}','{2}', '{3}')"
                cursor.execute(sql.format(employees[0], employees[1], employees[2], employees[3]))
                self.conexion.commit()
                print("Se cargo correctamente el empleado\n")

            except Error as ex:
                print("Error al intentar conexion: {0}".format(ex))

#Agregar nuevo producto Base de datos  
    def nuevoProducto(self, products):
          if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO products (namesProduct, stock, price) VALUES ('{0}','{1}','{2}')"
                cursor.execute(sql.format(products[0], products[1], products[2]))
                self.conexion.commit()
                print("Se cargo correctamente el producto\n")

            except Error as ex:
                print("Error al intentar conexion: {0}".format(ex))

#Funcion de Eliminar Producto
    def deleteProducto(self, eliminarProducto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM products WHERE idProducts = '{0}'"
                cursor.execute(sql.format(eliminarProducto))
                self.conexion.commit()
                print("Se elimino el Producto correctamente\n")

            except Error as ex:
                print("Error al intentar conexion: {0}".format(ex))

#Funcion de Eliminar Cliente
    def deleteCliente(self, eliminarCliente):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM clients WHERE dni = '{0}'"
                cursor.execute(sql.format(eliminarCliente))
                self.conexion.commit()
                print("Se elimino el Cliente correctamente\n")

            except Error as ex:
                print("Error al intentar conexion: {0}".format(ex))