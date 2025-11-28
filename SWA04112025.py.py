import tkinter as tk
from tkinter import ttk

def mostrar_pagina(pagina):
    print(f"Vas a la página: {pagina}")

def pagina_registro(frame):
    for w in frame.winfo_children(): w.destroy()
    tk.Label(frame, text="Registro de usuario", bg="#7499FF", fg="white",
             font=("Arial", 16, "bold")).pack(pady=10)
    campos = ["Nombre", "Edad", "Correo"]
    for c in campos:
        tk.Label(frame, text=c+":", bg="#6164FF", fg="white").pack()
        tk.Entry(frame, width=30).pack(pady=3)
    ttk.Button(frame, text="Continuar",
               command=lambda: mostrar_pagina("Test")).pack(pady=10)

root = tk.Tk()
root.title("Registro")
root.geometry("300x300")
frame = tk.Frame(root, bg="#A6BEFF")
frame.pack(fill="both", expand=True)
pagina_registro(frame)
root.mainloop()
