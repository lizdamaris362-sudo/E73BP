import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage 

# función que se ejecuta al presionar el botón
def iniciar_test():
    messagebox.showinfo("Inicio del test", "Bienvenido al test de adicciones")
    ventanabienv.destroy()

# configurar la ventana
ventanabienv = tk.Tk()
ventanabienv.title("IU Bienvenida")
ventanabienv.geometry("600x400") 
ventanabienv.config(bg="#3DDFFF",)
# centrar en pantalla
ancho_pantalla = ventanabienv.winfo_screenwidth()
alto_pantalla = ventanabienv.winfo_screenheight()
x = (ancho_pantalla // 2) - (600 // 2)
y = (alto_pantalla // 2) - (400 // 2)
ventanabienv.geometry(f"700x450+{x}+{y}")

# título principal
titulo = tk.Label(
    ventanabienv,
    text="BIENVENIDOS A MI SOFTWARE DE DETECCIÓN DE ADICCIONES A LAS REDES SOCIALES",
    font=("DM Serif Display", 18, "bold"),
    bg="#8C69FF",
    fg="#3DDFFF",
    wraplength=550,
    justify="center"
)
titulo.pack(pady=10)

# insertar una imagen
try:
    imagen = PhotoImage(file="AdiccionALasRedes.png")
    img_label = tk.Label(ventanabienv, image=imagen, bg="#048BDF")
    img_label.pack(pady=10)
except Exception:
    aviso = tk.Label(ventanabienv, text="No se encontró la imagen", bg="#026FF6")
    aviso.pack()

# texto descripción 
texto = tk.Label(
    ventanabienv,
    text="Nos da gusto tenerte aqui.Este espacio esta echo para ayudarte a tomar el control de tu tiempo y dejar de depender tanto de las redes sociales.",
    font=("DM Serif Display", 12),
    bg="#0425FE",
    fg="#00B7D7",
    wraplength=500,
    justify="center"
)
texto.pack(pady=20)

# botón para iniciar el test
boton_iniciar = tk.Button(
    ventanabienv,
    text="Iniciar TEST",
    font=("DM Serif Display", 14, "bold"),
    bg="#4CB9FC",
    fg="blue",
    relief="raised",
    bd=3,
    padx=20,
    pady=10,
    command=iniciar_test
)
boton_iniciar.pack(pady=10)

# ejecutar la interfaz
ventanabienv.mainloop()