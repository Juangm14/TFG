import csv
import requests
import os
import concurrent.futures

def descargar_imagen(image_url, image_path):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(image_path, 'wb') as image_file:
                image_file.write(response.content)
                print(f'Imagen descargada desde {image_url}: {os.path.basename(image_path)}')
        else:
            print(f'Error al descargar la imagen desde {image_url}. Código de estado: {response.status_code}')
    except Exception as e:
        print(f'Error al descargar la imagen desde {image_url}: {e}')

def procesar_archivo_csv(csv_file, csv_directory, max_imagenes=1500):
    # Creamos un directorio con el nombre del archivo CSV (sin la extensión)
    csv_name = os.path.splitext(os.path.basename(csv_file))[0]
    output_directory = os.path.join(csv_directory, csv_name)
    
    # Verificamos si el directorio de salida ya existe
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        
        # Inicializamos el contador
        counter = 0
        
        # Abrimos el archivo CSV
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            # Creamos una lista de trabajos pendientes
            trabajos_pendientes = []
            
            # Recorremos cada fila del archivo CSV
            for row in csv_reader:
                if counter >= max_imagenes:
                    break
                
                image_url = row['image_url']
                if image_url:
                    # Obtenemos la extensión de la imagen
                    extension = image_url.split('.')[-1]
                    # Generamos el nombre de la imagen
                    image_name = f'{counter+1}.{extension}'
                    # Path completo de la imagen
                    image_path = os.path.join(output_directory, image_name)
                    # Añadimos el trabajo a la lista de trabajos pendientes
                    trabajos_pendientes.append((image_url, image_path))
                    counter += 1
            
            # Procesamos los trabajos pendientes en paralelo
            with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
                for image_url, image_path in trabajos_pendientes:
                    executor.submit(descargar_imagen, image_url, image_path)
    else:
        print(f'Las imágenes ya están descargadas para {csv_name}')

def procesar_archivos_csv(csv_directory, max_imagenes=1500):
    # Lista todos los archivos CSV en el directorio
    csv_files = [os.path.join(csv_directory, file) for file in os.listdir(csv_directory) if file.endswith('.csv')]
    
    # Procesa cada archivo CSV en paralelo
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(procesar_archivo_csv, csv_file, csv_directory, max_imagenes): csv_file for csv_file in csv_files}
        for future in concurrent.futures.as_completed(futures):
            csv_file = futures[future]
            try:
                future.result()
            except Exception as e:
                print(f'Error al procesar {csv_file}: {e}')

if __name__ == "__main__":
    # Ruta del directorio que contiene los archivos CSV
    csv_directory = r'C:\Users\johns\Desktop\TFG\Dataset\CSV'
    # Descarga como máximo 1500 imágenes de cada archivo CSV
    procesar_archivos_csv(csv_directory, max_imagenes=1500)
