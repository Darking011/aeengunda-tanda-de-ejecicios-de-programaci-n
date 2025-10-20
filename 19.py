import tkinter as tk
from tkinter import messagebox

# --- Funciones del cifrado ---
def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            resultado += chr((ord(caracter) - base + desplazamiento) % 26 + base)
        else:
            resultado += caracter
    return resultado

def descifrar_cesar(texto, desplazamiento):
    return cifrar_cesar(texto, -desplazamiento)

# --- Función principal de interfaz ---
def ejecutar(opcion):
    texto = entrada_texto.get()
    try:
        desplazamiento = int(entrada_desplazamiento.get())
    except ValueError:
        messagebox.showerror("Error", "El desplazamiento debe ser un número entero.")
        return

    if opcion == "cifrar":
        resultado = cifrar_cesar(texto, desplazamiento)
    else:
        resultado = descifrar_cesar(texto, desplazamiento)

    salida_texto.delete(0, tk.END)
    salida_texto.insert(0, resultado)

# --- Ventana principal ---
ventana = tk.Tk()
ventana.title("Cifrado César")
ventana.geometry("400x300")

# --- Widgets ---
tk.Label(ventana, text="Texto a cifrar o descifrar:").pack(pady=5)
entrada_texto = tk.Entry(ventana, width=50)
entrada_texto.pack()

tk.Label(ventana, text="Desplazamiento:").pack(pady=5)
entrada_desplazamiento = tk.Entry(ventana, width=10)
entrada_desplazamiento.pack()

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Cifrar", command=lambda: ejecutar("cifrar")).pack(side=tk.LEFT, padx=10)
tk.Button(frame_botones, text="Descifrar", command=lambda: ejecutar("descifrar")).pack(side=tk.LEFT, padx=10)

tk.Label(ventana, text="Resultado:").pack(pady=5)
salida_texto = tk.Entry(ventana, width=50)
salida_texto.pack()

ventana.mainloop()
