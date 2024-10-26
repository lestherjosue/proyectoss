import subprocess
import tkinter as tk
from tkinter import messagebox
import os

# Directorio donde están los archivos de algoritmos
ALGORITMOS_DIR = 'algoritmos'  # Asegúrate de que esta carpeta existe y tiene los archivos

# Funciones para mostrar diferentes proyectos
def mostrar_algoritmos():
    # Limpiamos el frame principal
    limpiar_frame()

    # Crear botones para los diferentes proyectos en la carpeta algoritmos
    btn_clientes = tk.Button(frame, text="Clientes", command=lambda: abrir_algoritmo('clientes.py'))
    btn_clientes.pack(pady=5)

    btn_inventario = tk.Button(frame, text="Inventario", command=lambda: abrir_algoritmo('inventario.py'))
    btn_inventario.pack(pady=5)

    btn_reportes = tk.Button(frame, text="Reportes", command=lambda: abrir_algoritmo('reportes.py'))
    btn_reportes.pack(pady=5)

    btn_ventas = tk.Button(frame, text="Ventas", command=lambda: abrir_algoritmo('ventas.py'))
    btn_ventas.pack(pady=5)

    # Botón para volver al menú principal
    btn_volver = tk.Button(frame, text="Volver al menú principal", command=mostrar_menu_principal)
    btn_volver.pack(pady=10)

def abrir_algoritmo(archivo):
    try:
        # Crear la ruta completa del archivo dentro de la carpeta algoritmos
        archivo_path = os.path.join(ALGORITMOS_DIR, archivo)
        subprocess.run(["python", archivo_path])
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir el archivo {archivo}: {e}")

def mostrar_algebra_lineal():
    messagebox.showinfo("Mostrando", "Abriendo el proyecto de Álgebra Lineal...")
    subprocess.run(["python", "algebralineal.py"])

def mostrar_matematica_discreta():
    messagebox.showinfo("Mostrando", "Abriendo el proyecto de Matemática Discreta...")
    subprocess.run(["python", "matematica_discreta.py"])

def salir():
    root.destroy()

def limpiar_frame():
    # Limpiar el frame eliminando todos los widgets
    for widget in frame.winfo_children():
        widget.destroy()

def mostrar_menu_principal():
    # Limpiamos el frame principal
    limpiar_frame()

    # Crear botones del menú principal
    btn_algoritmos = tk.Button(frame, text="Mostrar Algoritmos", command=mostrar_algoritmos)
    btn_algoritmos.pack(pady=10)

    btn_algebra = tk.Button(frame, text="Mostrar Álgebra Lineal", command=mostrar_algebra_lineal)
    btn_algebra.pack(pady=10)

    btn_matematica = tk.Button(frame, text="Mostrar Matemática Discreta", command=mostrar_matematica_discreta)
    btn_matematica.pack(pady=10)

    btn_salir = tk.Button(frame, text="Salir", command=salir)
    btn_salir.pack(pady=10)

# Crear la ventana principal
root = tk.Tk()
root.title("Proyecto Matemático")
root.configure(bg='red')  # Establecer el fondo rojo

# Crear un frame para centrar los botones
frame = tk.Frame(root, bg='red')  # Asegurarse de que el frame también tenga fondo rojo
frame.pack(expand=True)

# Mostrar el menú principal al iniciar
mostrar_menu_principal()

# Ejecutar la aplicación
root.mainloop()
