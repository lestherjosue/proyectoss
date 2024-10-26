import sys
import math
from itertools import permutations, combinations, combinations_with_replacement
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit, QLabel, QHBoxLayout

class CombinatoriaApp(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Permutaciones y Combinaciones")
        self.setGeometry(100, 100, 500, 500)

        # Layout principal
        layout = QVBoxLayout()

        # Campos para ingresar valores de n y r
        self.label_n = QLabel("Valor de n:")
        self.input_n = QLineEdit(self)
        self.label_r = QLabel("Valor de r:")
        self.input_r = QLineEdit(self)

        # Layout horizontal para n y r
        layout_n_r = QHBoxLayout()
        layout_n_r.addWidget(self.label_n)
        layout_n_r.addWidget(self.input_n)
        layout_n_r.addWidget(self.label_r)
        layout_n_r.addWidget(self.input_r)

        layout.addLayout(layout_n_r)

        # Área de texto para mostrar resultados
        self.resultado = QTextEdit(self)
        self.resultado.setReadOnly(True)
        layout.addWidget(self.resultado)

        # Botones
        self.boton_permutaciones_sin_rep = QPushButton("Permutaciones sin repetición", self)
        self.boton_permutaciones_sin_rep.clicked.connect(self.mostrar_permutaciones_sin_repeticion)
        layout.addWidget(self.boton_permutaciones_sin_rep)

        self.boton_permutaciones_con_rep = QPushButton("Permutaciones con repetición", self)
        self.boton_permutaciones_con_rep.clicked.connect(self.mostrar_permutaciones_con_repeticion)
        layout.addWidget(self.boton_permutaciones_con_rep)

        self.boton_combinaciones_sin_rep = QPushButton("Combinaciones sin repetición", self)
        self.boton_combinaciones_sin_rep.clicked.connect(self.mostrar_combinaciones_sin_repeticion)
        layout.addWidget(self.boton_combinaciones_sin_rep)

        self.boton_combinaciones_con_rep = QPushButton("Combinaciones con repetición", self)
        self.boton_combinaciones_con_rep.clicked.connect(self.mostrar_combinaciones_con_repeticion)
        layout.addWidget(self.boton_combinaciones_con_rep)

        # Configuración final del layout
        self.setLayout(layout)

    def depurar(self, mensaje):
        """Función para depurar y mostrar mensajes en el área de texto."""
        self.resultado.append(mensaje)

    def obtener_valores(self):
        """Función para obtener y validar los valores de n y r."""
        try:
            n = int(self.input_n.text())
            r = int(self.input_r.text())
            return n, r
        except ValueError:
            self.depurar("Por favor, ingresa valores válidos para n y r.")
            return None, None

    def mostrar_permutaciones_sin_repeticion(self):
        n, r = self.obtener_valores()
        if n is not None and r is not None:
            resultado = permutaciones_sin_repeticion(n, r)
            self.depurar(f"Permutaciones sin repetición (P({n}, {r})): {resultado}")
            self.depurar("\nPermutaciones de elementos (sin repetición):")
            elementos = [chr(i) for i in range(65, 65 + n)]  # Generar elementos como 'A', 'B', 'C', etc.
            for p in permutations(elementos, r):
                self.depurar(str(p))

    def mostrar_permutaciones_con_repeticion(self):
        n, r = self.obtener_valores()
        if n is not None and r is not None:
            resultado = permutaciones_con_repeticion(n, r)
            self.depurar(f"Permutaciones con repetición (P({n}, {r})): {resultado}")

    def mostrar_combinaciones_sin_repeticion(self):
        n, r = self.obtener_valores()
        if n is not None and r is not None:
            resultado = combinaciones_sin_repeticion(n, r)
            self.depurar(f"Combinaciones sin repetición (C({n}, {r})): {resultado}")
            self.depurar("\nCombinaciones de elementos (sin repetición):")
            elementos = [chr(i) for i in range(65, 65 + n)]
            for c in combinations(elementos, r):
                self.depurar(str(c))

    def mostrar_combinaciones_con_repeticion(self):
        n, r = self.obtener_valores()
        if n is not None and r is not None:
            resultado = combinaciones_con_repeticion(n, r)
            self.depurar(f"Combinaciones con repetición (C({n}, {r})): {resultado}")
            self.depurar("\nCombinaciones de elementos (con repetición):")
            elementos = [chr(i) for i in range(65, 65 + n)]
            for cr in combinations_with_replacement(elementos, r):
                self.depurar(str(cr))


def permutaciones_sin_repeticion(n, r):
    return math.factorial(n) // math.factorial(n - r)

def permutaciones_con_repeticion(n, r):
    return n ** r

def combinaciones_sin_repeticion(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def combinaciones_con_repeticion(n, r):
    return math.factorial(n + r - 1) // (math.factorial(r) * math.factorial(n - 1))

# Ejecución de la aplicación
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ventana = CombinatoriaApp()
    ventana.show()
    sys.exit(app.exec_())
