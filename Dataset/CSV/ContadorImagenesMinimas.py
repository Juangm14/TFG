import os
from PIL import Image

def obtener_tamaño_imagen(ruta_imagen):
    """
    Esta función recibe la ruta de una imagen y devuelve su tamaño en bytes.
    """
    try:
        tamaño = os.path.getsize(ruta_imagen)
        return tamaño
    except FileNotFoundError:
        return f"No se pudo encontrar la imagen en la ruta especificada: {ruta_imagen}"

def obtener_dimensiones_imagen(ruta_imagen):
    """
    Esta función recibe la ruta de una imagen y devuelve sus dimensiones en píxeles.
    """
    try:
        with Image.open(ruta_imagen) as img:
            ancho, alto = img.size
            return ancho, alto
    except FileNotFoundError:
        return f"No se pudo encontrar la imagen en la ruta especificada: {ruta_imagen}"

if __name__ == "__main__":
    ruta_carpeta = input("Introduce la ruta de la carpeta: ")
    for ruta_raiz, carpetas, archivos in os.walk(ruta_carpeta):
        for archivo in archivos:
            if archivo.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                ruta_completa = os.path.join(ruta_raiz, archivo)
                if os.path.isfile(ruta_completa):
                    ancho, alto = obtener_dimensiones_imagen(ruta_completa)
                    tamaño = obtener_tamaño_imagen(ruta_completa)
                    if ancho > 224 and alto > 224:
                        print(f"Nombre del archivo: {archivo}")
                        print(f"Dimensiones de la imagen: {ancho}x{alto} píxeles")
                        print(f"Tamaño de la imagen en bytes: {tamaño} bytes")
                        print("-" * 50)
                    else:
                        print(f"La imagen {archivo} no cumple con las dimensiones mínimas de 224x224 píxeles.")
                        print("-" * 50)
