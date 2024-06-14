import os
import matplotlib.pyplot as plt

def contar_elementos_en_carpeta(ruta):
    contador = 0
    for _, _, archivos in os.walk(ruta):
        contador += len(archivos)
    return contador

train_data_dir = r'C:\Users\johns\Desktop\TFG\Dataset\train'
validation_data_dir = r'C:\Users\johns\Desktop\TFG\Dataset\valid'
test_data_dir = r'C:\Users\johns\Desktop\TFG\Dataset\test'

carpetas_train = os.listdir(train_data_dir)
carpetas_valid = os.listdir(validation_data_dir)
carpetas_test = os.listdir(test_data_dir)

datos = {}

for carpeta in carpetas_train:
    if carpeta in carpetas_valid and carpeta in carpetas_test:
        ruta_carpeta_train = os.path.join(train_data_dir, carpeta)
        ruta_carpeta_valid = os.path.join(validation_data_dir, carpeta)
        ruta_carpeta_test = os.path.join(test_data_dir, carpeta)
        elementos_train = contar_elementos_en_carpeta(ruta_carpeta_train)
        elementos_valid = contar_elementos_en_carpeta(ruta_carpeta_valid)
        elementos_test = contar_elementos_en_carpeta(ruta_carpeta_test)
        total_elementos = elementos_train + elementos_valid + elementos_test
        datos[carpeta] = total_elementos

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(datos.keys(), datos.values(), color='skyblue')
plt.xlabel('Clase')
plt.ylabel('Cantidad de Imágenes')
plt.title('Cantidad de imágenes por clase')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
