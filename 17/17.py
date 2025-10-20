from PIL import Image
import numpy as np

# --- 1. Cargar la imagen ---
ruta =ruta = "C:/Users/NET USO ESCOLAR 115/Pictures/sunset-6136876_1280.jpg"
imagen = Image.open(ruta)

# --- 2. Convertir a matriz ---
matriz = np.array(imagen)

# --- 3. Aplicar el filtro gris ---
# Calcular el promedio de los tres canales
gris = np.mean(matriz[:, :, :3], axis=2)  # promedio de R, G, B
# Repetir el valor del gris en los tres canales
matriz_gris = np.stack((gris, gris, gris), axis=2).astype(np.uint8)

# --- 4. Convertir de nuevo a imagen ---
imagen_gris = Image.fromarray(matriz_gris)

# --- 5. Mostrar las imágenes ---
imagen.show(title="Original")
imagen_gris.show(title="Escala de grises")

# --- 6. (Opcional) Guardar el resultado ---
guardar = input("¿Desea guardar la imagen en gris? (s/n): ")
if guardar.lower() == "s":
    imagen_gris.save("imagen_gris.png")
    print("Imagen guardada como 'imagen_gris.png'")
