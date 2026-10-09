import tkinter as tk
# USO DE IA: Este código base fue estructurado con asistencia de IA (Gemini),
# implementando las funciones básicas de dibujo, interfaz gráfica con tkinter y manejo de eventos del mouse,

# Variables globales para el estado del dibujo
color_actual = "black"
herramienta_actual = "lapiz"
x_anterior = None
y_anterior = None

def iniciar_dibujo(evento):
    # Función que detecta el primer clic del mouse
    global x_anterior, y_anterior
    x_anterior = evento.x
    y_anterior = evento.y

def dibujar(evento):
    # Función que dibuja en el lienzo mientras se mueve el mouse con el clic presionado
    global x_anterior, y_anterior, color_actual, herramienta_actual
    
    # Se utiliza un condicional básico (if) para confirmar que haya un punto inicial de dibujo
    if x_anterior and y_anterior:
        color_trazo = "white" if herramienta_actual == "borrador" else color_actual
        grosor = 10 if herramienta_actual == "borrador" else 2
        
        # create_line es la función de tkinter para dibujar líneas entre dos puntos
        lienzo.create_line(x_anterior, y_anterior, evento.x, evento.y, 
                           width=grosor, fill=color_trazo, capstyle=tk.ROUND, smooth=True)
        x_anterior = evento.x
        y_anterior = evento.y

def soltar_dibujo(evento):
    # Función que reinicia las coordenadas cuando se suelta el clic para que las líneas no se unan
    global x_anterior, y_anterior
    x_anterior = None
    y_anterior = None

def cambiar_color(nuevo_color):
    # Función para actualizar el color elegido por el usuario
    global color_actual, herramienta_actual
    color_actual = nuevo_color
    herramienta_actual = "lapiz"

def usar_borrador():
    # Función para cambiar al modo borrador
    global herramienta_actual
    herramienta_actual = "borrador"

def limpiar_pantalla():
    # Función para llenar/borrar todo el lienzo de color blanco
    lienzo.delete("all")

# Configuración principal de la ventana
ventana = tk.Tk()
ventana.title("Boceto de Paint - Entrega 2 ECI")

# Frame para los botones (Interfaz gráfica)
frame_herramientas = tk.Frame(ventana, bg="lightgray")
frame_herramientas.pack(side=tk.TOP, fill=tk.X)

# Creación de los botones de 8 colores usando un bucle for y listas
colores = ["black", "red", "blue", "green", "yellow", "orange", "purple", "brown"]
for col in colores:
    # lambda c=col: cambiar_color(c) se usa para pasarle un argumento a la función en un botón
    btn = tk.Button(frame_herramientas, bg=col, width=2, command=lambda c=col: cambiar_color(c))
    btn.pack(side=tk.LEFT, padx=2, pady=5)

# Botones de herramientas
btn_borrador = tk.Button(frame_herramientas, text="Borrador", command=usar_borrador)
btn_borrador.pack(side=tk.LEFT, padx=5, pady=5)

btn_limpiar = tk.Button(frame_herramientas, text="Limpiar Pantalla", command=limpiar_pantalla)
btn_limpiar.pack(side=tk.LEFT, padx=5, pady=5)

# Creación del lienzo (Canvas) donde se va a dibujar. Resolución 600x400
lienzo = tk.Canvas(ventana, width=600, height=400, bg="white")
lienzo.pack(pady=10)

# Detección de eventos del mouse (Proceso 6)
# <Button-1> detecta cuando se presiona el clic izquierdo
# <B1-Motion> detecta cuando se mueve el mouse con el clic izquierdo presionado
# <ButtonRelease-1> detecta cuando se suelta el clic izquierdo
lienzo.bind("<Button-1>", iniciar_dibujo)
lienzo.bind("<B1-Motion>", dibujar)
lienzo.bind("<ButtonRelease-1>", soltar_dibujo)

# Ejecutar el programa
ventana.mainloop()
