import subprocess
import sys
import os
import shutil
import datetime

from colorama import init, Fore, Style

def comprobar_y_crear_carpetas(rutas):
    #Comprueba si las carpetas en la lista existen, y si no, las crea.
    for ruta in rutas:
        if not os.path.exists(ruta):
            os.makedirs(ruta)

# Obtener la fecha y hora actual
def establecer_fecha():
    fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d')    
    with open('./info/fecha.txt', 'w') as archivo:
        archivo.write(fecha_actual)

# Obtener la fecha y hora actual
def obtener_fecha():
    with open('./info/fecha.txt', 'r') as archivo:
        fecha_actual = archivo.readline()
    return str(fecha_actual)

def check_and_install_ubuntu_package(package):
    """
    Comprueba si un paquete de Ubuntu está instalado y lo instala si no lo está.
    """
    try:
        subprocess.run(['dpkg', '-s', package], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(Fore.GREEN + f"El paquete de Ubuntu '{package}' ya está instalado.")
    except subprocess.CalledProcessError:
        print(Fore.RED + f"El paquete de Ubuntu '{package}' no está instalado. Instalando...")
        subprocess.check_call(['sudo', 'apt', 'install', package])

def check_and_install_python_package(package):
    """
    Comprueba si un paquete de Python está instalado y lo instala si no lo está.
    """
    try:
        __import__(package)
        print(Fore.GREEN + f"El paquete de Python '{package}' ya está instalado.")
    except ImportError:
        print(Fore.RED + f"El paquete de Python '{package}' no está instalado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip3", "install", package])

def check_and_install_dependencies(ubuntu_packages, python_packages):
    """
    Comprueba e instala los paquetes necesarios de Ubuntu y Python.
    """
    for package in ubuntu_packages:
        check_and_install_ubuntu_package(package)
    
    for package in python_packages:
        check_and_install_python_package(package)

def comprobar_contenido_y_eliminar(rutas =  ["./info/","./evidencias/"]):
    #Comprueba si las carpetas tienen contenido y ofrece la opción de eliminar su contenido.    
    for ruta in rutas:
        if os.path.exists(ruta):
            contenido = os.listdir(ruta)
            if contenido:
                print(Fore.GREEN + f"La carpeta '{ruta}' tiene contenido.")
                print(Fore.RED + f"Si continúa, se borrarán todos los datos de análisis anteriores.")
                opcion = input(Fore.RED + f"¿Deseas eliminar el contenido de la carpeta '{ruta}'? (s/n): ").strip().lower()
                if opcion == 's':
                    for item in contenido:
                        item_path = os.path.join(ruta, item)
                        if os.path.isdir(item_path):
                            shutil.rmtree(item_path)
                        else:
                            os.remove(item_path)
                    print(f"Contenido de la carpeta '{ruta}' eliminado.")
                    shutil.rmtree(ruta)
                else:
                    print(f"Contenido de la carpeta '{ruta}' no eliminado.")
                    shutil.rmtree(ruta)
            else:
                #print(f"La carpeta '{ruta}' está vacía.")
                shutil.rmtree(ruta)
        else:
            print(f"La carpeta '{ruta}' no existe.")

if __name__ == "__main__":
    establecer_fecha()