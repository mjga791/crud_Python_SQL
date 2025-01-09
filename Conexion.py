# Lo primero es instalar el paquete mysql-connector-python. 
# Para ello, abrimos una terminal (CTRL + Ñ) y escribimos el siguiente comando:
# pip install mysql-connector-python

# Además, tenemos que importar esta librería en nuestro código Python
import mysql.connector

class CConexion:
    def ConexionBaseDeDatos(self):
        try:
            # Conectar a la base de datos
            conexion = mysql.connector.connect(user='root', password='',
                                               host='127.0.0.1', 
                                               database='clientesdb',  
                                               port='3306')  
            print("Conexión establecida")
            return conexion    
            
        except mysql.connector.Error as error:
            print("Error de conexión a MySQL: {}".format(error))
            return None

# Crear una instancia de la clase y llamar al método
conexion = CConexion()
conexion.ConexionBaseDeDatos()