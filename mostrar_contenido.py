import os
from utils import obtener_fecha

fecha = obtener_fecha()

def mostrar_contenido_carpeta(rutas = [
    "./info/" + str(fecha),
    "./evidencias/" + str(fecha)
    ]):
    #Muestra el contenido de las carpetas especificadas.
    for ruta in rutas:
        if os.path.exists(ruta):
            contenido = os.listdir(ruta)
            if contenido:
                print(f"\nContenido de la carpeta '{ruta}':")
                for item in contenido:
                    item_path = os.path.join(ruta, item)
                    if os.path.isfile(item_path):
                        #mostrar_menu_archivo(item_path)
                        mostrar_contenido_archivo(item_path)
                    else:
                        print(f"Directorio: {item}")
            else:
                print(f"\nLa carpeta '{ruta}' está vacía.")
        else:
            print(f"\nLa carpeta '{ruta}' no existe.")

def mostrar_menu_archivo(ruta_archivo):
    #Muestra un menú con el nombre del archivo antes de mostrar su contenido.
    print(f"\n--- Menú: {os.path.basename(ruta_archivo)} ---")
    #input("Presiona Enter para ver el contenido del archivo...")

def mostrar_contenido_archivo(ruta_archivo):
    #Muestra el contenido del archivo especificado.
    print(f"\nContenido del archivo '{ruta_archivo}':")
    with open(ruta_archivo, 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
    #print("\n--- Fin del contenido ---\n")

# Lista de rutas de carpetas a comprobar
carpetas = [
    "./info/" + str(fecha),
    "./evidencias/" + str(fecha)
]

# Llamada a la función para mostrar el contenido de las carpetas
#mostrar_contenido_carpeta(carpetas)
