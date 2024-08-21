import tkinter as tk

ventana = tk.Tk()
ventana.geometry("350x250+550+150")
ventana.config(bg="thistle1")
ventana.title("Prueba positivo/negativo")
ventana.iconbitmap("zero_two.ico")

label1 = tk.Label(
    ventana, text="Comprueba si tu numero es Positivo o Negativo!!!")
label1.pack()

label2 = tk.Label(
    ventana, text="Ingresa El numero")
label2.pack()


def texto_a_mostrar():

    try:
        texto = float(texto_varibale.get())

        if texto > 0:
            resultado.set("El Numero Es Positivo")
        elif texto == 0:
            resultado.set("Su numero es 0!")
        else:
            resultado.set("Su Numero Es Negativo")

    except ValueError:
        resultado.set("El valor no es un número válido")


texto_varibale = tk.StringVar()


resultado = tk.StringVar()


entrada_texto = tk.Entry(ventana, textvariable=texto_varibale)
entrada_texto.pack()

boton_resultado = tk.Button(ventana, text="Presiona", command=texto_a_mostrar)
boton_resultado.pack()

etiqueta_resultado = tk.Label(ventana, textvariable=resultado)
etiqueta_resultado.pack()


ventana.mainloop()
