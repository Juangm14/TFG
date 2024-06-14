import os
from PIL import Image

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
    ruta_carpeta = r"C:\Users\johns\Desktop\TFG\Dataset\train"
    for ruta_raiz, carpetas, archivos in os.walk(ruta_carpeta):
        for archivo in archivos:
            if archivo.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                ruta_completa = os.path.join(ruta_raiz, archivo)
                if os.path.isfile(ruta_completa):
                    ancho, alto = obtener_dimensiones_imagen(ruta_completa)
                    if ancho <= 224 and alto <= 224:
                        print(f"La imagen {archivo} tiene dimensiones menores a 224x224 píxeles.")
