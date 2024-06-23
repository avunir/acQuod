import datetime
from colorama import init
from dependencias import check_and_install_dependencies, comprobar_y_crear_carpetas
from utils import limpiar_pantalla, seleccionar_dispositivo
from bloqueo import montaje
from menu import menu_principal

# Inicializa colorama
init(autoreset=True)

if __name__ == "__main__":
    
    #Comprobamos dependencias necesarias para ejecutar el programa
    # Lista de paquetes de Ubuntu y Python a comprobar
    ubuntu_packages = ['gddrescue', 'util-linux', 'vim-common', 'dislocker', 'xxd', 'gddrescue']  # Paquetes de Ubuntu
    python_packages = ['numpy', 'os']  # Paquetes de Python
    check_and_install_dependencies(ubuntu_packages, python_packages)
    
    #Comprobamos si las carpetas necesarias existen, y si no, las crea.
    comprobar_y_crear_carpetas(['./info/','./evidencias/'])
    #Inicializamos la fecha
    fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d')
    with open('./info/fecha.txt', 'w') as archivo:
        archivo.write(fecha_actual)

    #Comprobamos que el sistema operativo bloquea el acceso a los dispositivos externos
    montaje()    
    
    limpiar_pantalla()
    
    
    #Ofrecemos al usuario elegir el dispositivo
    dispositivo = seleccionar_dispositivo()
    #particiones = utils.listar_particiones(dispositivo)
    #print(particiones)
    #esperar_pulsacion_tecla()
    
    #iniciamos el menu principal
    menu_principal()
