
import sqlite3
from typing import List, Dict, Union


class ModeloProductos:

    def connect(self):
        """
            Función que se contecta a la base de datos y permite interactuar con ella con el cursor
            todas las clases siguientes la invocan
        """
       
        try:
            
            self.conn = sqlite3.connect('productos.db')
            self.cursor = self.conn.cursor()
       
        except sqlite3.Error as error:
            return f"Ocurrió un error {error}"

    def listaProductos(self) -> List[Dict[str, Union[int, float, str]]]:
        """
            Función que se encarga de devolver todos los productos de la base de datos
            devuelve una lista con diccionarios dentro
        """
        
        response = []
       
        try:
            
            self.connect()
            self.cursor.execute('SELECT * FROM productos')
            
            for row in self.cursor:
                product = {
                    "id_productos":row[0],
                    "nombre":row[1],
                    "descripción":row[2],
                    "imagen": row[3],
                    "extension": row[4],
                    "precio":row[5],
                    "existencias":row[6]
                    }
                
                response.append(product)
            self.conn.close()
        
        except sqlite3.Error as error:
            print(f"Ocurrió un error: {error} - 201 | Modelo")
        return response

    def detalleProductos(self, idProducto: str) -> List[Dict[str, Union[int, float, str]]]:
        """
            Función que se encarga de devolver los datos de un producto en base a su id
            devolviendo una lista con un diccionario del producto dentro
        """
        
        response = []
        
        try:
            
            self.connect()
            self.cursor.execute('SELECT * FROM productos WHERE id_productos = ?', (idProducto, ))
            
            for row in self.cursor:
                product = {
                    "id_productos":row[0],
                    "nombre":row[1],
                    "descripción":row[2],
                    "imagen":row[3],
                    "extension": row[4],
                    "precio":row[5],
                    "existencias":row[6]
                    }
                
                response.append(product)
            self.conn.close()
        
        except sqlite3.Error as error:
            print(f"Ocurrió un error: {error} - 202 | Modelo")
        return response

    def insertarProductos(self, producto: Dict[str, Union[int, float, str]]) -> bool:
        """
            Función que se encarga de insertar un nuevo producto en la base de datos, recibe un diccionario
            con los datos del producto correspondiete y devuelve un resultado booleano
        """
        
        respuesta = False
        
        try:
            
            self.connect()
            self.cursor.execute('INSERT INTO productos (nombre, descripcion, imagen, extension, precio, existencias) VALUES (?, ?, ?, ?, ?, ?)', (producto["nombre"], producto["descripcion"], producto["imagen"], producto["extension"], float(producto["precio"]), int(producto["existencia"])))
            
            result = self.cursor.rowcount
            
            if result:
                respuesta = True
            
            self.conn.commit()
            self.conn.close()
       
        except sqlite3.Error as error:
            print(f"Ocurrió un error: {error} - 203 | Modelo")
        return respuesta

    def actualizarProductos(self, producto: Dict[str, Union[int, float, str]]) -> bool:
        """
            Funciión que se encarga de actualizar un producto en la base de datos, recibe los datos actualizados
            del producto en un diccionario para luego ser subidos a la base de datos, devuelve una respuesta
            booleana
        """
        
        response = False
       
        try:
            
            self.connect()
            
            self.cursor.execute("""UPDATE productos SET nombre = ?, descripcion = ?, imagen = ?, extension = ?,  precio = ?, existencias = ?
                                WHERE id_productos = ?""", (producto["nombre"], producto["descripcion"], producto["imagen"], producto["extension"],
                                                            float(producto["precio"]), producto["existencia"], int(producto["producto"])))
            result = self.cursor.rowcount
            
            if result:
                response = True
            
            self.conn.commit()
            self.conn.close()
        
        except sqlite3.Error as error:
            print(f"Ocurrió un error {error} - 204| Modelo")
        return response

    def borrarProductos(self, idProducto: str) -> bool:
        """
            Función que se encarga de borrar un producto de la base de datos, recibe el identificador del producto
            a eliminar y devuelve un booleano
        """
        
        result = False
        
        try:
            
            self.connect()
            self.cursor.execute('DELETE FROM productos WHERE id_productos = ?', (idProducto, ))
            
            filas_afectadas = self.cursor.rowcount
          
            self.conn.commit()
            self.conn.close()
            
            if filas_afectadas > 0:
                result = True
        
        except sqlite3.Error as error:
            print(f"Ocurrió un eror: {error} - 205 | Modelo")
        return result


    def buscarProductos(self, nombreProducto: str) -> List[Dict[str, Union[int, float, str]]]:
        """
            Función que se encarga de buscar un producto en base a su nombre, esta función no es sensible a mayúsculas
            ni a minúsculas, solamente al ordén y los espacios, recibe el nombre y devuelve el producto encontrado en un
            diccionario
        """
        
        resultado = []
        
        try:
           
            self.connect()
            nombreProducto = nombreProducto.lower()
           
            self.cursor.execute('SELECT * FROM productos WHERE LOWER(nombre) LIKE ?', ('%' + nombreProducto + '%',))
            
            for row in self.cursor:
                producto = {
                    "id_productos":row[0],
                    "nombre":row[1],
                    "descripción":row[2],
                    "imagen":row[3],
                    "extension": row[4],
                    "precio":row[5],
                    "existencias":row[6]
                    }
                
                resultado.append(producto)
            self.conn.close()
        
        except sqlite3.Error as error:
            print(f"Ocurrió un error: {error} - 206 | Modelo")
        return resultado