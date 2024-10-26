import sys
from graphviz import Digraph

class Producto:
    def __init__(self, codigo, nombre, existencia, proveedor, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.existencia = existencia
        self.proveedor = proveedor
        self.precio = precio

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Existencia: {self.existencia}, Proveedor: {self.proveedor}, Precio: {self.precio} USD"

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        """ Agregar un nuevo producto al inventario """
        self.productos.append(producto)

    def listar_productos(self):
        """ Mostrar todos los productos en inventario """
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos:
                print(producto)

    def actualizar_producto(self, codigo, nombre=None, existencia=None, proveedor=None, precio=None):
        """ Actualizar los detalles de un producto """
        for producto in self.productos:
            if producto.codigo == codigo:
                if nombre: producto.nombre = nombre
                if existencia is not None: producto.existencia = existencia
                if proveedor: producto.proveedor = proveedor
                if precio is not None: producto.precio = precio
                print(f"Producto con código {codigo} actualizado.")
                return
        print(f"Producto con código {codigo} no encontrado.")

    def editar_existencias(self, codigo, nueva_existencia):
        """ Editar las existencias de un producto """
        for producto in self.productos:
            if producto.codigo == codigo:
                producto.existencia = nueva_existencia
                print(f"Existencia del producto con código {codigo} actualizada.")
                return
        print(f"Producto con código {codigo} no encontrado.")

    def eliminar_producto(self, codigo):
        """ Eliminar un producto del inventario """
        for producto in self.productos:
            if producto.codigo == codigo:
                self.productos.remove(producto)
                print(f"Producto con código {codigo} eliminado.")
                return
        print(f"Producto con código {codigo} no encontrado.")

    def generar_diagrama_flujo(self):
        """Genera un diagrama de flujo más completo de las operaciones del inventario"""
        dot = Digraph(comment='Diagrama de Flujo del Inventario')

        # Nodos principales del sistema
        dot.node('I', 'Inventario (Inicio)')
        dot.node('AP', 'Agregar Producto')
        dot.node('LP', 'Listar Productos')
        dot.node('UP', 'Actualizar Producto')
        dot.node('EP', 'Editar Existencias')
        dot.node('DP', 'Eliminar Producto')
        dot.node('F', 'Fin del Proceso')

        # Agregar productos como nodos
        for producto in self.productos:
            dot.node(producto.codigo, f'Producto: {producto.nombre}\nExistencia: {producto.existencia}\nPrecio: ${producto.precio}')
            dot.edge('AP', producto.codigo)

        # Relacionar los nodos de operaciones
        dot.edge('I', 'AP', label="Nuevo producto")
        dot.edge('I', 'LP', label="Ver productos")
        dot.edge('I', 'UP', label="Modificar producto")
        dot.edge('I', 'EP', label="Actualizar existencias")
        dot.edge('I', 'DP', label="Eliminar producto")
        dot.edge('AP', 'F', label="Producto agregado")
        dot.edge('UP', 'F', label="Producto actualizado")
        dot.edge('EP', 'F', label="Existencias editadas")
        dot.edge('DP', 'F', label="Producto eliminado")
        dot.edge('LP', 'F', label="Lista completa")

        # Guardar el archivo en formato PDF o PNG
        dot.render('diagrama_flujo_inventario', format='pdf')
        print("Diagrama de flujo generado y guardado como 'diagrama_flujo_inventario.pdf'.")

# Funciones para interactuar con el inventario
def menu():
    inventario = Inventario()

    while True:
        print("\n----- Menú de Control de Inventario -----")
        print("1. Crear producto")
        print("2. Listar productos")
        print("3. Actualizar producto")
        print("4. Editar existencias")
        print("5. Eliminar producto")
        print("6. Generar diagrama de flujo")
        print("7. Salir")
        
        opcion = input("Elige una opción (1-7): ")

        if opcion == "1":
            codigo = input("Código del producto: ")
            nombre = input("Nombre del producto: ")
            existencia = int(input("Cantidad en existencia: "))
            proveedor = input("Proveedor: ")
            precio = float(input("Precio del producto: "))
            producto = Producto(codigo, nombre, existencia, proveedor, precio)
            inventario.agregar_producto(producto)
            print(f"Producto {nombre} agregado al inventario.")

        elif opcion == "2":
            print("\nLista de productos:")
            inventario.listar_productos()

        elif opcion == "3":
            codigo = input("Código del producto a actualizar: ")
            print("Deja en blanco los campos que no deseas actualizar.")
            nombre = input("Nuevo nombre (deja en blanco para no cambiar): ")
            existencia = input("Nueva existencia (deja en blanco para no cambiar): ")
            existencia = int(existencia) if existencia else None
            proveedor = input("Nuevo proveedor (deja en blanco para no cambiar): ")
            precio = input("Nuevo precio (deja en blanco para no cambiar): ")
            precio = float(precio) if precio else None
            inventario.actualizar_producto(codigo, nombre, existencia, proveedor, precio)

        elif opcion == "4":
            codigo = input("Código del producto: ")
            nueva_existencia = int(input("Nueva cantidad en existencia: "))
            inventario.editar_existencias(codigo, nueva_existencia)

        elif opcion == "5":
            codigo = input("Código del producto a eliminar: ")
            inventario.eliminar_producto(codigo)

        elif opcion == "6":
            inventario.generar_diagrama_flujo()

        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    menu()
