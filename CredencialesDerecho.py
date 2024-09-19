import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Programa de credenciales de la facultad de derecho y estudios políticos")

# Definir el tamaño de la ventana
ventana.geometry("600x600")

# Añadir una etiqueta
etiqueta = tk.Label(ventana, text="¡Hola, esta es una ventana de Tkinter!", font=("Arial", 14))
etiqueta.pack(pady=20)

# Añadir un botón
boton = tk.Button(ventana, text="Cerrar", command=ventana.quit)
boton.pack(pady=10)

# Iniciar el bucle principal
ventana.mainloop()
