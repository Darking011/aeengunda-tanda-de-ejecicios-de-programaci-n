def cifrado_cesar(mensaje, desplazamiento):
    resultado = ""
    for caracter in mensaje:
        if caracter.isalpha():  # Si es una letra
            base = ord('A') if caracter.isupper() else ord('a')
            nueva_letra = chr((ord(caracter) - base + desplazamiento) % 26 + base)
            resultado += nueva_letra
        else:
            resultado += caracter  # Deja igual los espacios y símbolos
    return resultado


# --- Programa principal ---
mensaje = input("Ingrese el mensaje: ")
desplazamiento = int(input("Ingrese el desplazamiento (use número negativo para descifrar): "))

resultado = cifrado_cesar(mensaje, desplazamiento)

if desplazamiento >= 0:
    print("Mensaje cifrado:", resultado)
else:
    print("Mensaje descifrado:", resultado)
