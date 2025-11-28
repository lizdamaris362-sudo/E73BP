#importar las librerias
import tkinter as tk 
def mostrar_ventana2 ():
    ventana1.withdraw() #esta funcion sirve npara que oculte la ventana 1
    ventana2.deiconify() # muestra la ventana 2
def regresar ():
    ventana2.wthdraw() # esta funcion sirva para que oculte la ventana 2
    ventana1.deiconify() # muestre la ventana 1

#creacion de ventana 1
ventana1= tk.Tk()
label1=tk.Label(ventana1,text ="Esta ventana numero 1")
ventana1.geometry("600x400")
label1.pack()
btn1=tk.Button(ventana1, text ="ir a la ventana 2", command= mostrar_ventana2)
btn1.pack()

#creacion de ventana 2
ventana2= tk.Tk()
label2=tk.Label(ventana2, text="Esta es la ventana numero 2")
ventana2.geometry("300x300")
label2.pack()
btn2=tk.Button(ventana2, text="ir ala ventana 1" ,command= regresar)
btn2.pack()
ventana2.withdraw()

#creacion de ventanas (lanzar la interfaz)
ventana1.mainloop()