import tkinter as tk
import random

# --- Ventana ---
app = tk.Tk()
app.geometry("400x500")
app.title("Adivina el número")

# --- Variables ---
entrada = tk.StringVar()
salida = tk.StringVar()
intentos = tk.IntVar()

# Generar número secreto
def nuevo_juego():
    global numero_secreto
    numero_secreto = random.randint(1, 20)
    entrada.set("")
    salida.set("He pensado un número entre 1 y 20")
    intentos.set(0)

def adivina():
    try:
        intento = int(entrada.get())
        if intento < 1 or intento > 20:
            salida.set("⚠️ Solo números del 1 al 20")
            return

        intentos.set(intentos.get() + 1)  # sumar intento

        if intento == numero_secreto:
            salida.set(f"🎉 ¡Correcto! Lo lograste en {intentos.get()} intentos")
            nuevo_juego()  # reiniciar automáticamente
        elif intento < numero_secreto:
            salida.set("El número secreto es mayor 🔼")
        else:
            salida.set("El número secreto es menor 🔽")
    except ValueError:
        salida.set("⚠️ Ingresa un número válido")

# --- Widgets ---
tk.Label(
    app, text="Adivina el número secreto entre el 1 y el 20", font=("Arial", 12)
).pack(pady=10)

tk.Entry(
    app, textvariable=entrada, font=("Arial", 14), justify="center"
).pack(pady=10)

tk.Button(
    app, text="Probar", command=adivina, font=("Arial", 12)
).pack(pady=5)

tk.Button(
    app, text="Nuevo Juego", command=nuevo_juego, font=("Arial", 12)
).pack(pady=5)

tk.Label(
    app, textvariable=salida, font=("Arial", 12), fg="blue"
).pack(pady=10)

# Iniciar juego
nuevo_juego()

# --- Loop principal ---
app.mainloop()
