import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QComboBox, QGridLayout
from PyQt5.QtGui import QPalette, QColor

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Operaciones con Matrices y Sistemas de Ecuaciones")
        self.setGeometry(100, 100, 600, 400)

        # Establecer color de fondo
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#ADD8E6"))  # Color azul claro
        self.setPalette(palette)

        layout = QVBoxLayout()

        self.inversa_btn = QPushButton("Encontrar la Inversa de una Matriz", self)
        self.inversa_btn.setFixedHeight(50)
        self.inversa_btn.clicked.connect(self.abrirInversa)
        layout.addWidget(self.inversa_btn)

        self.multiplicacion_btn = QPushButton("Multiplicación de Matrices", self)
        self.multiplicacion_btn.setFixedHeight(50)
        self.multiplicacion_btn.clicked.connect(self.abrirMultiplicacion)
        layout.addWidget(self.multiplicacion_btn)

        self.sistemas_btn = QPushButton("Resolver Sistemas de Ecuaciones", self)
        self.sistemas_btn.setFixedHeight(50)
        self.sistemas_btn.clicked.connect(self.abrirSistemas)
        layout.addWidget(self.sistemas_btn)

        self.setLayout(layout)

    def abrirInversa(self):
        self.inversa_window = InversaWindow()
        self.inversa_window.show()

    def abrirMultiplicacion(self):
        self.multiplicacion_window = MultiplicacionWindow()
        self.multiplicacion_window.show()

    def abrirSistemas(self):
        self.sistemas_window = SistemasWindow()
        self.sistemas_window.show()


class InversaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Inversa de una Matriz")
        self.setGeometry(150, 150, 400, 300)

        # Color de fondo
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#ADD8E6"))  # Color azul claro
        self.setPalette(palette)

        layout = QVBoxLayout()

        self.label = QLabel("Introduce la matriz (3 números por columna):")
        layout.addWidget(self.label)

        self.matriz_inputs = QGridLayout()
        for i in range(3):  # 3 filas
            for j in range(3):  # 3 columnas
                input_field = QLineEdit(self)
                input_field.setFixedWidth(50)  # Ancho fijo para cada entrada
                self.matriz_inputs.addWidget(input_field, i, j)

        layout.addLayout(self.matriz_inputs)

        self.result_btn = QPushButton("Calcular Inversa", self)
        self.result_btn.clicked.connect(self.calcularInversa)
        layout.addWidget(self.result_btn)

        self.graph_btn = QPushButton("Graficar Inversa", self)
        self.graph_btn.clicked.connect(self.graficarInversa)
        layout.addWidget(self.graph_btn)

        self.result_label = QLabel("Resultado:")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calcularInversa(self):
        try:
            matriz = np.array([[float(self.matriz_inputs.itemAtPosition(i, j).widget().text()) for j in range(3)] for i in range(3)])
            inversa = np.linalg.inv(matriz)
            self.result_label.setText(f"Inversa: \n{inversa}")
            self.inversa_matrix = inversa  # Guardamos la inversa para graficar
        except np.linalg.LinAlgError:
            self.result_label.setText("La matriz no tiene inversa.")
        except Exception as e:
            self.result_label.setText(f"Error: {str(e)}")

    def graficarInversa(self):
        if hasattr(self, 'inversa_matrix'):
            plt.imshow(self.inversa_matrix, cmap='hot', interpolation='nearest')
            plt.title('Inversa de la Matriz')
            plt.colorbar()
            plt.show()
        else:
            self.result_label.setText("Primero calcula la inversa.")


class MultiplicacionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Multiplicación de Matrices")
        self.setGeometry(150, 150, 400, 300)

        # Color de fondo
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#98FB98"))  # Color verde claro
        self.setPalette(palette)

        layout = QVBoxLayout()

        self.label1 = QLabel("Introduce la primera matriz (3 números por columna):")
        layout.addWidget(self.label1)

        self.matriz1_inputs = QGridLayout()
        for i in range(3):  # 3 filas
            for j in range(3):  # 3 columnas
                input_field = QLineEdit(self)
                input_field.setFixedWidth(50)
                self.matriz1_inputs.addWidget(input_field, i, j)

        layout.addLayout(self.matriz1_inputs)

        self.label2 = QLabel("Introduce la segunda matriz (3 números por columna):")
        layout.addWidget(self.label2)

        self.matriz2_inputs = QGridLayout()
        for i in range(3):  # 3 filas
            for j in range(3):  # 3 columnas
                input_field = QLineEdit(self)
                input_field.setFixedWidth(50)
                self.matriz2_inputs.addWidget(input_field, i, j)

        layout.addLayout(self.matriz2_inputs)

        self.result_btn = QPushButton("Multiplicar", self)
        self.result_btn.clicked.connect(self.multiplicarMatrices)
        layout.addWidget(self.result_btn)

        self.graph_btn = QPushButton("Graficar Producto", self)
        self.graph_btn.clicked.connect(self.graficarProducto)
        layout.addWidget(self.graph_btn)

        self.result_label = QLabel("Resultado:")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def multiplicarMatrices(self):
        try:
            matriz1 = np.array([[float(self.matriz1_inputs.itemAtPosition(i, j).widget().text()) for j in range(3)] for i in range(3)])
            matriz2 = np.array([[float(self.matriz2_inputs.itemAtPosition(i, j).widget().text()) for j in range(3)] for i in range(3)])
            producto = np.dot(matriz1, matriz2)
            self.result_label.setText(f"Producto: \n{producto}")
            self.product_matrix = producto  # Guardamos el producto para graficar
        except ValueError:
            self.result_label.setText("Error: Las matrices deben ser compatibles para la multiplicación.")
        except Exception as e:
            self.result_label.setText(f"Error: {str(e)}")

    def graficarProducto(self):
        if hasattr(self, 'product_matrix'):
            plt.imshow(self.product_matrix, cmap='hot', interpolation='nearest')
            plt.title('Producto de las Matrices')
            plt.colorbar()
            plt.show()
        else:
            self.result_label.setText("Primero multiplica las matrices.")


class SistemasWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Resolver Sistemas de Ecuaciones")
        self.setGeometry(150, 150, 400, 400)

        # Color de fondo
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#FFD700"))  # Color dorado claro
        self.setPalette(palette)

        layout = QVBoxLayout()

        self.label = QLabel("Selecciona el método:")
        layout.addWidget(self.label)

        self.metodo_combo = QComboBox(self)
        self.metodo_combo.addItem("Gauss-Jordan")
        self.metodo_combo.addItem("Regla de Cramer")
        layout.addWidget(self.metodo_combo)

        self.matriz_label = QLabel("Matriz de coeficientes (3 números por columna):")
        layout.addWidget(self.matriz_label)

        self.matriz_inputs = QGridLayout()
        for i in range(3):  # 3 filas
            for j in range(3):  # 3 columnas
                input_field = QLineEdit(self)
                input_field.setFixedWidth(50)
                self.matriz_inputs.addWidget(input_field, i, j)

        layout.addLayout(self.matriz_inputs)

        self.vector_label = QLabel("Vector de términos independientes (3 números por columna):")
        layout.addWidget(self.vector_label)

        self.vector_inputs = QGridLayout()
        for i in range(3):  # 3 filas
            input_field = QLineEdit(self)
            input_field.setFixedWidth(50)
            self.vector_inputs.addWidget(input_field, i, 0)  # 1 columna para el vector

        layout.addLayout(self.vector_inputs)

        self.result_btn = QPushButton("Resolver", self)
        self.result_btn.clicked.connect(self.resolverSistema)
        layout.addWidget(self.result_btn)

        self.graph_btn = QPushButton("Graficar Soluciones", self)
        self.graph_btn.clicked.connect(self.graficarSoluciones)
        layout.addWidget(self.graph_btn)

        self.result_label = QLabel("Resultado:")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def resolverSistema(self):
        try:
            matriz = np.array([[float(self.matriz_inputs.itemAtPosition(i, j).widget().text()) for j in range(3)] for i in range(3)])
            vector = np.array([float(self.vector_inputs.itemAtPosition(i, 0).widget().text()) for i in range(3)])
            if self.metodo_combo.currentText() == "Gauss-Jordan":
                soluciones = np.linalg.solve(matriz, vector)
                self.result_label.setText(f"Soluciones: {soluciones}")
                self.soluciones = soluciones  # Guardamos las soluciones para graficar
            elif self.metodo_combo.currentText() == "Regla de Cramer":
                determinante = np.linalg.det(matriz)
                if determinante == 0:
                    self.result_label.setText("El sistema no tiene solución única.")
                else:
                    soluciones = np.linalg.solve(matriz, vector)
                    self.result_label.setText(f"Soluciones: {soluciones}")
                    self.soluciones = soluciones  # Guardamos las soluciones para graficar
        except Exception as e:
            self.result_label.setText(f"Error: {str(e)}")

    def graficarSoluciones(self):
        if hasattr(self, 'soluciones'):
            plt.plot(self.soluciones, marker='o')
            plt.title('Soluciones del Sistema de Ecuaciones')
            plt.xlabel('Variables')
            plt.ylabel('Valores de Solución')
            plt.xticks(range(len(self.soluciones)), [f'x{i+1}' for i in range(len(self.soluciones))])
            plt.grid()
            plt.show()
        else:
            self.result_label.setText("Primero resuelve el sistema.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
