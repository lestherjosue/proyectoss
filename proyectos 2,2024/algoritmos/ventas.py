import sys
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton,
    QLineEdit, QLabel, QMessageBox, QTabWidget, QFormLayout
)
from graphviz import Digraph


class ClienteManager:
    def __init__(self):
        self.clientes = []

    def crear_cliente(self, codigo, nombre, direccion):
        cliente = {"codigo": codigo, "nombre": nombre, "direccion": direccion}
        self.clientes.append(cliente)

    def listar_clientes(self):
        return self.clientes


class Producto:
    def __init__(self, codigo, nombre, existencia, proveedor, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.existencia = existencia
        self.proveedor = proveedor
        self.precio = precio


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)


class Ventas:
    def __init__(self):
        self.df = pd.DataFrame(columns=['cliente', 'producto', 'cantidad', 'precio_unitario'])

    def agregar_venta(self, cliente, producto, cantidad, precio_unitario):
        nueva_venta = pd.DataFrame([{
            'cliente': cliente, 'producto': producto, 'cantidad': cantidad, 'precio_unitario': precio_unitario
        }])
        self.df = pd.concat([self.df, nueva_venta], ignore_index=True)

    def generar_diagrama_flujo(self):
        try:
            dot = Digraph(comment='Flujo de Gestión de Ventas')
            dot.node('A', 'Inicio')
            dot.node('B', 'Registrar Cliente')
            dot.node('C', 'Registrar Producto')
            dot.node('D', 'Registrar Venta')
            dot.node('E', 'Fin')
            dot.edges(['AB', 'AC', 'AD', 'DE'])

            output_file = 'flujo_gestion_ventas'
            dot.render(output_file, format='png', cleanup=True)
            QMessageBox.information(None, "Éxito", f"Diagrama de flujo generado exitosamente: {output_file}.png")
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Ocurrió un error al generar el diagrama: {str(e)}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Ventas")
        self.setGeometry(100, 100, 600, 400)

        # Instancias de clases de gestión
        self.cliente_manager = ClienteManager()
        self.inventario = Inventario()
        self.ventas = Ventas()

        # Inicializar interfaz gráfica
        self.init_ui()

    def init_ui(self):
        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)

        # Tab para clientes
        cliente_tab = QWidget()
        self.tabs.addTab(cliente_tab, "Clientes")
        cliente_layout = QVBoxLayout()
        cliente_tab.setLayout(cliente_layout)

        # Formulario para clientes
        form_cliente = QFormLayout()
        self.codigo_cliente_input = QLineEdit()
        self.nombre_cliente_input = QLineEdit()
        self.direccion_cliente_input = QLineEdit()
        form_cliente.addRow("Código:", self.codigo_cliente_input)
        form_cliente.addRow("Nombre:", self.nombre_cliente_input)
        form_cliente.addRow("Dirección:", self.direccion_cliente_input)
        cliente_layout.addLayout(form_cliente)

        # Botón para crear cliente
        btn_crear_cliente = QPushButton('Crear Cliente')
        btn_crear_cliente.clicked.connect(self.crear_cliente)
        cliente_layout.addWidget(btn_crear_cliente)

        # Tab para productos
        producto_tab = QWidget()
        self.tabs.addTab(producto_tab, "Productos")
        producto_layout = QVBoxLayout()
        producto_tab.setLayout(producto_layout)

        form_producto = QFormLayout()
        self.codigo_producto_input = QLineEdit()
        self.nombre_producto_input = QLineEdit()
        self.existencias_producto_input = QLineEdit()
        self.proveedor_producto_input = QLineEdit()
        self.precio_producto_input = QLineEdit()
        form_producto.addRow("Código:", self.codigo_producto_input)
        form_producto.addRow("Nombre:", self.nombre_producto_input)
        form_producto.addRow("Existencias:", self.existencias_producto_input)
        form_producto.addRow("Proveedor:", self.proveedor_producto_input)
        form_producto.addRow("Precio:", self.precio_producto_input)
        producto_layout.addLayout(form_producto)

        btn_crear_producto = QPushButton('Crear Producto')
        btn_crear_producto.clicked.connect(self.crear_producto)
        producto_layout.addWidget(btn_crear_producto)

        # Tab para ventas
        venta_tab = QWidget()
        self.tabs.addTab(venta_tab, "Ventas")
        venta_layout = QVBoxLayout()
        venta_tab.setLayout(venta_layout)

        form_venta = QFormLayout()
        self.cliente_venta_input = QLineEdit()
        self.producto_venta_input = QLineEdit()
        self.cantidad_venta_input = QLineEdit()
        self.precio_venta_input = QLineEdit()
        form_venta.addRow("Cliente:", self.cliente_venta_input)
        form_venta.addRow("Producto:", self.producto_venta_input)
        form_venta.addRow("Cantidad:", self.cantidad_venta_input)
        form_venta.addRow("Precio Unitario:", self.precio_venta_input)
        venta_layout.addLayout(form_venta)

        btn_agregar_venta = QPushButton('Agregar Venta')
        btn_agregar_venta.clicked.connect(self.agregar_venta)
        venta_layout.addWidget(btn_agregar_venta)

        # Botón para generar diagrama de flujo
        btn_diagrama_flujo = QPushButton('Generar Diagrama de Flujo')
        btn_diagrama_flujo.clicked.connect(self.ventas.generar_diagrama_flujo)
        venta_layout.addWidget(btn_diagrama_flujo)

    def crear_cliente(self):
        codigo = self.codigo_cliente_input.text()
        nombre = self.nombre_cliente_input.text()
        direccion = self.direccion_cliente_input.text()

        if codigo and nombre and direccion:
            self.cliente_manager.crear_cliente(codigo, nombre, direccion)
            QMessageBox.information(self, "Éxito", "Cliente creado exitosamente.")
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")

    def crear_producto(self):
        codigo = self.codigo_producto_input.text()
        nombre = self.nombre_producto_input.text()
        existencia = self.existencias_producto_input.text()
        proveedor = self.proveedor_producto_input.text()
        precio = self.precio_producto_input.text()

        if codigo and nombre and existencia and proveedor and precio:
            producto = Producto(codigo, nombre, int(existencia), proveedor, float(precio))
            self.inventario.agregar_producto(producto)
            QMessageBox.information(self, "Éxito", "Producto creado exitosamente.")
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")

    def agregar_venta(self):
        cliente = self.cliente_venta_input.text()
        producto = self.producto_venta_input.text()
        cantidad = self.cantidad_venta_input.text()
        precio = self.precio_venta_input.text()

        if cliente and producto and cantidad.isdigit() and precio.replace('.', '', 1).isdigit():
            self.ventas.agregar_venta(cliente, producto, int(cantidad), float(precio))
            QMessageBox.information(self, "Éxito", "Venta agregada exitosamente.")
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos correctamente.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
