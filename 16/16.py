from PIL import Image
import numpy as np

# --- Cargar la imagen ---
ruta = "C:\\Users\\NET USO ESCOLAR 115\\Pictures\\sunset-6136876_1280.jpg"


# Abrimos la imagen
imagen = Image.open(ruta)

# Convertimos a matriz (numpy array)
matriz = np.array(imagen)
print("Matriz de la imagen cargada con forma:", matriz.shape)

# --- Preguntar al usuario ---
print("Opciones de rotación:")
print("1. Rotar 90° a la izquierda")
print("2. Rotar 90° a la derecha")
print("3. Rotar 180°")

opcion = input("Seleccione una opción (1, 2 o 3): ")

# --- Función para rotar ---
def rotar_imagen(img, opcion):
    if opcion == "1":
        return img.rotate(90, expand=True)
    elif opcion == "2":
        return img.rotate(-90, expand=True)
    elif opcion == "3":
        return img.rotate(180, expand=True)
    else:
        print("Opción no válida.")
        return img

# --- Aplicar rotación ---
imagen_rotada = rotar_imagen(imagen, opcion)

# --- Mostrar imágenes ---
imagen.show(title="Imagen Original")
imagen_rotada.show(title="Imagen Rotada")
