from menu import menu_principal
from utils import limpiar_pantalla, seleccionar_dispositivo
from dependencias import check_and_install_dependencies, establecer_fecha, comprobar_y_crear_carpetas
from bloqueo import montaje
from colorama import init, Fore, Style


# Inicializa colorama
init(autoreset=True)

if __name__ == "__main__":
    
    #Comprobamos dependencias necesarias para ejecutar el programa
    # Lista de paquetes de Ubuntu y Python a comprobar
    ubuntu_packages = ['gddrescue', 'util-linux', 'vim-common', 'dislocker']  # Paquetes de Ubuntu
    python_packages = ['numpy', 'os']  # Paquetes de Python
    check_and_install_dependencies(ubuntu_packages, python_packages)
    
    #Comprobamos que el sistema operativo bloquea el acceso a los dispositivos externos
    montaje()
    #Comprobamos que las carpetas de trabajo existen
    limpiar_pantalla()
    comprobar_y_crear_carpetas()
    #Inicializamos la fecha
    establecer_fecha()
    
    #Ofrecemos al usuario elegir el dispositivo
    dispositivo = seleccionar_dispositivo()
    
    #iniciamos el menu principal
    menu_principal()
