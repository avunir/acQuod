import os, datetime
from colorama import init

import dependencias, bloqueo, utils, menu

# Inicializa colorama
init(autoreset=True)

if __name__ == "__main__":
    
    #Comprobamos dependencias necesarias para ejecutar el programa
    # Lista de paquetes de Ubuntu y Python a comprobar
    ubuntu_packages = ['gddrescue', 'util-linux', 'vim-common', 'dislocker']  # Paquetes de Ubuntu
    python_packages = ['shutil', 'platform']  # Paquetes de Python
    dependencias.check_and_install_dependencies(ubuntu_packages, python_packages)
    
    #Inicializamos el contenido
    rutas = ['./info/','./evidencias/']
    #Comprueba si las carpetas en la lista existen, y si no, las crea.
    for ruta in rutas:
        if not os.path.exists(ruta):
            os.makedirs(ruta)
    #Inicializamos la fecha
    fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d')
    with open('./info/fecha.txt', 'w') as archivo:
        archivo.write(fecha_actual)
    #comprobar_contenido_y_eliminar()

    #Comprobamos que el sistema operativo bloquea el acceso a los dispositivos externos
    bloqueo.montaje()    
    
    utils.limpiar_pantalla()
    
    
    #Ofrecemos al usuario elegir el dispositivo
    dispositivo = utils.seleccionar_dispositivo()
    
    #iniciamos el menu principal
    menu.menu_principal()
