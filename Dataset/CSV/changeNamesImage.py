import os

# Establecer el número inicial
starting_number = 1

# Obtener el directorio actual
current_dir = os.getcwd()

# Cambiar al directorio de destino
os.chdir(r"C:\Users\johns\Desktop\TFG\Dataset\train\GOLONDRINA COMUN")

# Obtener una lista de todos los archivos en el directorio
files = os.listdir()

# Renombrar los archivos
for i, file in enumerate(files):
    # Obtener la extensión del archivo
    ext = os.path.splitext(file)[1]
    # Nuevo nombre del archivo
    new_filename = f"{starting_number + i}{ext}"
    # Renombrar el archivo
    os.rename(file, new_filename)

# Cambiar de nuevo al directorio original
os.chdir(current_dir)
