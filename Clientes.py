from Conexion import CConexion
import mysql.connector

class CCliente:
    # El decorador @staticmethod en Python se utiliza PARA DEFINIR UN MÉTODO ESTÁTICO
    # dentro de una clase. Un método estático es una función que pertenece a la clase,
    # pero no tiene acceso a la instancia de la clase (self) ni a la clase en sí (cls).
    # NO REQUIEREN UNA INSTANCIA: Puedes llamar a un método estático 
    # directamente desde la clase sin crear una instancia de la clase.
    # NO ACCEDEN A LA INSTANCIA NI A LA CLASE: Los métodos estáticos no pueden acceder 
    # a los atributos o métodos de instancia o de clase. Son útiles para agrupar funciones
    #  que tienen una relación lógica con la clase, pero no necesitan acceder a sus datos.
    # SE UTILIZAN PARA DEFINIR FUNCIONES UTILITARIAS, relacionadas con la clase, 
    # pero que no dependen de los atributos de la clase ni de sus instancias.

    # Cuando se define un método estático con @staticmethod, no necesitas self 
    # porque el método no interactúa con ninguna instancia de la clase. 
    # Sin embargo, cuando defines métodos que necesitan acceder o modificar 
    # los atributos de la instancia, self es necesario.
    @staticmethod
    def altaClientes(nombre, apellidos, nacionalidad):
        # Código para guardar el cliente en la base de datos
        print(f"Cliente guardado: {nombre} {apellidos}, Nacionalidad: {nacionalidad}")
        
        try:
            cone = CConexion().ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "insert into usuarios values (null, %s, %s, %s);"
            valores = (nombre, apellidos, nacionalidad)
            cursor.execute(sql, valores)
            cone.commit()
            cone.close()
            return cursor.lastrowid

        except mysql.connector.Error as error:
            print("Error en insercción de datos : {}".format(error))
            
    @staticmethod
    def mostrarClientes():
        try:
            cone = CConexion().ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from usuarios;")
            registros = cursor.fetchall()
            cone.close()
            return registros

        except mysql.connector.Error as error:
            print("Error en mostrar datos : {}".format(error))
            return []
        
    @staticmethod
    def modificarClientes(id, nombre, apellidos, nacionalidad):
        # Código para guardar el cliente en la base de datos
        print(f"Cliente modificado: {nombre} {apellidos}, Nacionalidad: {nacionalidad}")
        
        try:
            cone = CConexion().ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "UPDATE usuarios SET usuarios.nombre=%s,usuarios.apellidos=%s, usuarios.nacionalidad=%s WHERE usuarios.id=%s;"
            valores = (nombre, apellidos, nacionalidad, id)
            cursor.execute(sql, valores)
            cone.commit()
            print("Registro modificado correctamente")
            cone.close()
            
        except mysql.connector.Error as error:
            print("Error en actualización de datos : {}".format(error))    
        

    @staticmethod
    def eliminarClientes(id):
        # Código para guardar el cliente en la base de datos
        print(f"Cliente eliminado - ID: {id}")
        
        try:
            cone = CConexion().ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "DELETE FROM usuarios WHERE usuarios.id=%s;"
            # Para que sea una tupla, aunque sólo tenga un valor
            # debemos poner la , al final
            valores = (id,)
            cursor.execute(sql, valores)
            cone.commit()
            print("Registro eliminado correctamente")
            cone.close()
            
        except mysql.connector.Error as error:
            print("Error en eliminación de datos : {}".format(error))    
        