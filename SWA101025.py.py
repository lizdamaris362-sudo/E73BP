#importar la biblioteca
import tkinter as tk
from tkinter import ttk

#crear la venta la ventan de python 
ventana=tk.Tk()
ventana.title("esta es mi primera ventana")
ventana.geometry("300x400")
#agreagamos los widgets
ttk.Label(ventana,text="este es el equipo 7 y 9").grid(column=0,row=0)
#activamos la ventana 
ventana.resizable(0,0)
ventana.mainloop()
#agreagamos los widgets
ttk.Label(ventana,text="los numeros de los integrantes del equipo 7 son 5 y del equipo 9 son 5integrantes ) ").grid(column=0,row=0)
#activamos la ventana 
ventana.resizable(0,0)
ventana.mainloop()