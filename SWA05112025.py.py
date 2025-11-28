import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox

#--------CONFIGURACIÓN DE COLORES Y FUENTE --------
COLOR_FONDO = "#B90303"
COLOR_MENU = "#FF5D57"
COLOR_TEXTO = "#DA3535"
FUENTE_TITULO = ("DM Serif Display", 16, "bold")
FUENTE_TEXTO = ("DM Serif Display", 12)

#--------VENTANA PRINCIPAL----------
root = tk.Tk()
root.title("Bienestar Digital")
root.geometry("900x500")
root.config(bg=COLOR_FONDO)

#--------FRAME MENÚ LATERAL----------
menu_frame = tk.Frame(root, bg=COLOR_MENU, width=200)
menu_frame.pack(side="left", fill="y")

#-------- FRAME CONTENIDO------------
contenido_frame = tk.Frame(root, bg=COLOR_FONDO)
contenido_frame.pack(side="right", fill="both", expand=True)

#--------FUNCIÓN PARA CAMBIAR DE PÁGINA----------
def mostrar_pagina(nombre):
    for widget in contenido_frame.winfo_children():
        widget.destroy()
    paginas[nombre]()

#------PÁGINAS-----
def pagina_bienvenida():
    tk.Label(contenido_frame, text="Bienvenido a mi software de detección de adicciones a las redes sociales", 
             font=FUENTE_TITULO, bg=COLOR_FONDO, wraplength=700, fg="white").pack(pady=20)
    tk.Label(contenido_frame, text="Nos da gusto tenerte aquí. Este espacio está hecho para ayudarte a tomar el control de tu tiempo y dejar de depender tanto de las redes sociales.", 
             bg=COLOR_FONDO, font=FUENTE_TEXTO, wraplength=700, fg="white").pack(pady=10)

    # Imagen opcional
    try:
        imagen = PhotoImage(file="AdiccionALasRedes.png")
        img_label = tk.Label(contenido_frame, image=imagen, bg=COLOR_FONDO)
        img_label.image = imagen  # evitar garbage collector
        img_label.pack(pady=10)
    except Exception:
        tk.Label(contenido_frame, text="No se encontró la imagen", bg=COLOR_FONDO, fg="yellow").pack(pady=10)

    ttk.Button(contenido_frame, text="Continuar", command=lambda: mostrar_pagina("Registro")).pack(pady=20)

def pagina_registro():
    tk.Label(contenido_frame, text="Registro de usuario", font=FUENTE_TITULO, bg=COLOR_FONDO, fg="white").pack(pady=20)
    entradas = {}
    for campo in ["Nombre", "Edad", "Correo"]:
        tk.Label(contenido_frame, text=f"{campo}:", bg=COLOR_FONDO, font=FUENTE_TEXTO, fg="white").pack()
        entrada = tk.Entry(contenido_frame, width=40)
        entrada.pack(pady=5)
        entradas[campo] = entrada
    ttk.Button(contenido_frame, text="Continuar", command=lambda: mostrar_pagina("Test")).pack(pady=20)

# ---------- PÁGINA TEST ----------
def pagina_test():
    tk.Label(contenido_frame, text="Test de Bienestar", font=FUENTE_TITULO, bg=COLOR_FONDO, fg="white").pack(pady=20)
    tk.Label(contenido_frame, text="Responde las siguientes preguntas para conocer tu nivel de adicción a las redes sociales.", 
             wraplength=600, bg=COLOR_FONDO, font=FUENTE_TEXTO, fg="white").pack(pady=10)

    preguntas = [
        "1. ¿Con qué frecuencia revisas tus redes sociales al día?",
        "2. ¿Te sientes ansioso si no puedes revisar tus redes?",
        "3. ¿Pasas más de 3 horas diarias en redes sociales?",
        "4. ¿Te comparas constantemente con otros en redes?",
        "5. ¿Has intentado reducir el uso de redes sin éxito?"
    ]

    opciones = [
        ("Nunca", 0),
        ("A veces", 1),
        ("Frecuentemente", 2),
        ("Siempre", 3)
    ]

    respuestas = []

    for p in preguntas:
        tk.Label(contenido_frame, text=p, bg=COLOR_FONDO, font=FUENTE_TEXTO, fg="white", anchor="w").pack(pady=5)
        var = tk.IntVar(value=0)
        respuestas.append(var)
        for texto, val in opciones:
            tk.Radiobutton(contenido_frame, text=texto, value=val, variable=var,
                           bg=COLOR_FONDO, fg="white", selectcolor=COLOR_MENU).pack(anchor="w", padx=30)

    def mostrar_resultados():
        puntaje_total = sum(v.get() for v in respuestas)
        mostrar_resultado_sin_grafica(puntaje_total)

    ttk.Button(contenido_frame, text="Ver resultados", command=mostrar_resultados).pack(pady=20)

# ---------- RESULTADO SIN MATPLOTLIB ----------
def mostrar_resultado_sin_grafica(puntaje):
    for widget in contenido_frame.winfo_children():
        widget.destroy()

    tk.Label(contenido_frame, text="Resultados del Test", font=FUENTE_TITULO, bg=COLOR_FONDO, fg="white").pack(pady=20)

    # Determinar nivel de adicción
    if puntaje <= 4:
        nivel = "Bajo"
        color = "green"
        mensaje = "Tienes un uso saludable de las redes sociales. ¡Sigue así!"
    elif puntaje <= 8:
        nivel = "Moderado"
        color = "orange"
        mensaje = "Tu uso de redes es moderado, pero podrías beneficiarte de reducirlo un poco."
    else:
        nivel = "Alto"
        color = "red"
        mensaje = "Parece que pasas demasiado tiempo en redes sociales. Considera buscar equilibrio."

    tk.Label(contenido_frame, text=f"Nivel de adicción: {nivel}", font=FUENTE_TEXTO, bg=COLOR_FONDO, fg="white").pack(pady=10)
    tk.Label(contenido_frame, text=mensaje, font=FUENTE_TEXTO, wraplength=600, bg=COLOR_FONDO, fg="white").pack(pady=10)

    # Barra de progreso visual
    ttk.Label(contenido_frame, text="Tu nivel de adicción:", background=COLOR_FONDO, foreground="white").pack(pady=5)
    barra = ttk.Progressbar(contenido_frame, orient="horizontal", length=400, mode="determinate", maximum=15)
    barra.pack(pady=10)
    barra["value"] = puntaje

    # Colorear la barra según el nivel
    style = ttk.Style()
    style.theme_use("default")
    style.configure("green.Horizontal.TProgressbar", troughcolor="white", background="green")
    style.configure("orange.Horizontal.TProgressbar", troughcolor="white", background="orange")
    style.configure("red.Horizontal.TProgressbar", troughcolor="white", background="red")

    if nivel == "Bajo":
        barra.config(style="green.Horizontal.TProgressbar")
    elif nivel == "Moderado":
        barra.config(style="orange.Horizontal.TProgressbar")
    else:
        barra.config(style="red.Horizontal.TProgressbar")

    ttk.Button(contenido_frame, text="Volver al inicio", command=lambda: mostrar_pagina("Bienvenida")).pack(pady=20)

#-------Diccionario de páginas-------
paginas = {
    "Bienvenida": pagina_bienvenida,
    "Registro": pagina_registro,
    "Test": pagina_test,
}

#----------Botones de menú lateral----------
for nombre in paginas:
    ttk.Button(menu_frame, text=nombre, command=lambda n=nombre: mostrar_pagina(n)).pack(fill="x", pady=5, padx=10)

ttk.Button(menu_frame, text="Salir", command=root.quit).pack(side="bottom", pady=10)

#----------Mostrar página inicial--------
pagina_bienvenida()

root.mainloop()