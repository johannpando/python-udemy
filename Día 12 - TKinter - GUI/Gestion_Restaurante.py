import tkinter as tk
from tkinter import messagebox


# Función para calcular el total
def calcular_total():
    try:
        # Obtiene la cantidad ingresada
        cantidad = int(cantidad_entry.get())

        # Obtiene el precio del plato seleccionado
        plato_seleccionado = plato_var.get()
        precio_plato = menu[plato_seleccionado]

        # Calcula el total
        total = cantidad * precio_plato
        total_label.config(text=f"Total: ${total}")

        # Guardar el total para mostrarlo en el recibo
        return total
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese una cantidad válida.")


# Función para generar el recibo
def generar_recibo():
    total = calcular_total()
    if total:
        recibo_text.delete(1.0, tk.END)  # Limpiar el área de texto antes de escribir
        recibo_text.insert(tk.END, f"Recibo\n")
        recibo_text.insert(tk.END, f"Plato: {plato_var.get()}\n")
        recibo_text.insert(tk.END, f"Cantidad: {cantidad_entry.get()}\n")
        recibo_text.insert(tk.END, f"Total: ${total}\n")
        recibo_text.insert(tk.END, f"Gracias por su compra!")


# Función para agregar dígitos y operadores a la pantalla de la calculadora
def agregar_calculadora(valor):
    # Cambiamos temporalmente el estado a "normal" para poder modificar el contenido
    calculadora_display.config(state="normal")

    """
    Aquí te explico qué hacen los métodos `get()`, `delete()`, e `insert()` en el widget `Entry` de Tkinter:

    ### 1. **`get()`**:
    El método `get()` en el widget `Entry` se utiliza para obtener el texto que actualmente está contenido en ese campo.
    
    - Función: Recupera el texto actual que el campo `Entry` tiene en ese momento y lo almacena en la variable `actual`.
    - Uso típico: Se utiliza para obtener lo que el usuario ha escrito o lo que se ha mostrado en el campo de texto 
    hasta ese momento.
    
    ---
    
    ### 2. **`delete()`**:
    El método `delete()` se usa para eliminar parte o todo el contenido del widget `Entry`. Tiene dos parámetros:
    
    
    - **Parámetros**:
      - El primer parámetro es el índice de inicio del texto que deseas eliminar (por ejemplo, `0` para el primer 
      carácter).
      - El segundo parámetro es el índice del final del texto que deseas eliminar. Puedes usar `tk.END` para indicar 
      hasta el último carácter.
    
    - **Ejemplos**:
      - `delete(0, tk.END)`: Elimina todo el contenido del `Entry`.
      - `delete(3, 5)`: Elimina los caracteres entre los índices 3 y 5.
    
    En este caso, `delete(0, tk.END)` borra todo el contenido de `Entry`.
    
    ---
    
    ### 3. **`insert()`**:
    El método `insert()` se utiliza para agregar texto al campo `Entry` en una posición específica.
    
    - **Parámetros**:
      - El primer parámetro indica el índice donde se insertará el texto. Si usas `tk.END`, el texto se insertará al 
      final del contenido actual.
      - El segundo parámetro es el texto que deseas insertar.
    
    - **Ejemplo**:
      - `insert(0, "Hola")`: Inserta el texto `"Hola"` al principio del campo.
      - `insert(tk.END, "Mundo")`: Inserta el texto `"Mundo"` al final del contenido existente.
    
    En este caso, `insert(tk.END, actual + str(valor))` inserta el nuevo valor (`valor`) al final del contenido actual 
    (`actual`), construyendo así la expresión matemática.
    
    ---
    
    ### Resumen de lo que hacen juntos:
    
    - **`get()`** obtiene el texto actual del campo de entrada.
    - **`delete()`** borra el contenido del campo (en este caso, borra todo el texto).
    - **`insert()`** añade texto nuevo al campo, combinando el texto existente (`actual`) con el nuevo valor (`valor`). 
    Esto permite que la pantalla de la calculadora se actualice con los nuevos dígitos u operadores que el usuario está 
    introduciendo.
    """

    actual = calculadora_display.get()
    calculadora_display.delete(0, tk.END)
    calculadora_display.insert(tk.END, actual + str(valor))

    # Volvemos a deshabilitar la entrada para que el usuario no pueda escribir
    calculadora_display.config(state="disabled")


# Función de la calculadora
def calcular():
    try:
        # Cambiamos temporalmente el estado a "normal" para evaluar y modificar el contenido
        calculadora_display.config(state="normal")

        expresion = calculadora_display.get()
        resultado = eval(expresion)
        calculadora_display.delete(0, tk.END)
        calculadora_display.insert(tk.END, str(resultado))

        # Volvemos a deshabilitar la entrada
        calculadora_display.config(state="disabled")
    except:
        calculadora_display.config(state="normal")
        calculadora_display.delete(0, tk.END)
        calculadora_display.insert(tk.END, "Error")
        calculadora_display.config(state="disabled")


# Función para limpiar la pantalla de la calculadora
def resetear_calculadora():
    calculadora_display.config(state="normal")
    calculadora_display.delete(0, tk.END)
    calculadora_display.config(state="disabled")


# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Restaurante")
ventana.geometry("600x600")

# Menú del restaurante (platos y sus precios)
menu = {
    "Pizza": 10,
    "Hamburguesa": 8,
    "Ensalada": 5,
    "Sopa": 4
}

# Variables de control
plato_var = tk.StringVar(value="Pizza")
cantidad_var = tk.IntVar(value=1)

"""
El asterisco * en Python se conoce como operador de desempaquetado. 
En este contexto, su uso permite pasar los elementos del diccionario menu.keys() como argumentos 
individuales a la función OptionMenu, en lugar de pasar el objeto iterable dict_keys. 
Esto es necesario porque OptionMenu espera una lista de opciones como parámetros separados, no un solo objeto iterable.

Sin el asterisco: menu.keys() devuelve un objeto tipo dict_keys (un iterable) que no es lo que OptionMenu necesita.
Con el asterisco: *menu.keys() desempaqueta las claves del diccionario como argumentos separados. 
Por ejemplo, si menu es {"Pizza": 10, "Hamburguesa": 8}, el uso de *menu.keys() se convierte en "Pizza", "Hamburguesa".
"""
# Etiqueta y dropdown para seleccionar el plato
tk.Label(ventana, text="Seleccione un plato:").pack()
plato_menu = tk.OptionMenu(ventana, plato_var, *menu.keys())
"""
pack() es un método de geometría en Tkinter que gestiona la disposición de los widgets (elementos gráficos) 
en la ventana. Se usa para agregar widgets a la ventana principal o a un contenedor sin necesidad de especificar 
coordenadas precisas.

Al usar pack(), puedes organizar los widgets de una manera sencilla, alineándolos uno tras otro 
(arriba/abajo o izquierda/derecha).

Opciones de pack():
side: Define dónde se coloca el widget. Puede ser TOP (por defecto), LEFT, RIGHT, o BOTTOM.
fill: Estira el widget para ocupar todo el espacio horizontal (X), vertical (Y) o ambos (BOTH).
expand: Si es True, expande el widget para llenar el espacio disponible.
"""
plato_menu.pack()

# Entrada para la cantidad de platos
tk.Label(ventana, text="Cantidad:").pack()
cantidad_entry = tk.Entry(ventana, textvariable=cantidad_var, width=5)
cantidad_entry.pack()

# Botón para calcular el total
tk.Button(ventana, text="Calcular total", command=calcular_total).pack()

# Etiqueta para mostrar el total
total_label = tk.Label(ventana, text="Total: $0")
total_label.pack()

# Área de texto para el recibo
recibo_text = tk.Text(ventana, height=10, width=30)
recibo_text.pack()

# Botón para generar el recibo
tk.Button(ventana, text="Generar recibo", command=generar_recibo).pack()

# Separador para la calculadora
tk.Label(ventana, text="").pack()  # Espacio en blanco para separar la calculadora
tk.Label(ventana, text="Calculadora").pack()
# Calculadora
calculadora_display = tk.Entry(ventana, width=20, state="disabled")
calculadora_display.pack()

# Crear un Frame para los botones de la calculadora
calculadora_frame = tk.Frame(ventana)
calculadora_frame.pack()

# Botones de la calculadora con el uso de grid() en el Frame
botones_calculadora = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Añadir botones de la calculadora usando grid() para alinearlos en filas y columnas
for (texto, fila, columna) in botones_calculadora:
    if texto == '=':
        boton = tk.Button(calculadora_frame, text=texto, width=5, command=calcular)
    elif texto == 'C':
        boton = tk.Button(calculadora_frame, text=texto, width=5, command=resetear_calculadora)
    else:
        boton = tk.Button(calculadora_frame, text=texto, width=5, command=lambda t=texto: agregar_calculadora(t))

    boton.grid(row=fila, column=columna, padx=5, pady=5)

ventana.mainloop()
