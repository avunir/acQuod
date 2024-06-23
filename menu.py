import datetime
from colorama import Fore, Style
from analisis import mostrar_informacion_hardware, mostrar_informacion_software, mostrar_informacion_cifrado
from dependencias import comprobar_contenido_y_eliminar, comprobar_y_crear_carpetas
from utils import limpiar_pantalla, esperar_pulsacion_tecla, mostrar_contenido_carpeta, seleccionar_dispositivo, obtener_disco_seleccionado, ejecutar_comando
from adquisicion import adquirir_particiones
from bloqueo import montaje

def salir():
    # Función ficticia para el ejemplo
    print(Fore.RED + "Saliendo del programa...")
    ejecutar_comando(["sudo", "umount", "/mnt/forense*"])

def menu_principal():
    """Presenta el menú principal y gestiona las opciones del usuario."""
     
    titulo = """
                    ____                        _ 
                   / __ \                      | |
     __ _    ___  | |  | |  _   _    ___     __| |
    / _` |  / __| | |  | | | | | |  / _ \   / _` |
   | (_| | | (__  | |__| | | |_| | | (_) | | (_| |
    \__,_|  \___|  \___\_\  \__,_|  \___/   \__,_|
    """
   
    while True:
        print(Fore.CYAN + Style.BRIGHT + "\n" + "=" * 40)
        print(Fore.YELLOW + Style.BRIGHT + titulo)
        print(Fore.CYAN + Style.BRIGHT + "=" * 40)
        print(Fore.CYAN + "\nMenú principal:")
        print(Fore.CYAN + "1. Proceso de adquisición")
        print(Fore.CYAN + "2. Información hardware")
        print(Fore.CYAN + "3. Información software")
        print(Fore.CYAN + "4. Información cifrado")
        print(Fore.CYAN + "5. Mostrar información análisis anteriores")
        print(Fore.CYAN + "6. Eliminar información análisis anteriores y seleccionar un nuevo dispositivo")
        print(Fore.CYAN + "S. Salir")
        print(Fore.YELLOW + Style.BRIGHT + "\nDispositivo seleccionado: " + obtener_disco_seleccionado())
        print(Fore.CYAN + "=" * 40 + "\n")

        opcion = input(Fore.CYAN + "Selecciona una opción (1-6)(S salir): ")

        if opcion == "1":
            #mostrar_informacion_hardware() 
            #mostrar_informacion_software()
            #mostrar_informacion_cifrado()
            adquirir_particiones()
            limpiar_pantalla()
        elif opcion == "2":
            mostrar_informacion_hardware()
            esperar_pulsacion_tecla()
            limpiar_pantalla()
        elif opcion == "3":
            mostrar_informacion_software()
            esperar_pulsacion_tecla()
            limpiar_pantalla()
        elif opcion == "4":
            mostrar_informacion_cifrado()
            #esperar_pulsacion_tecla()
            limpiar_pantalla()
        elif opcion == "5":
            mostrar_contenido_carpeta()
            esperar_pulsacion_tecla()
            limpiar_pantalla()
        elif opcion == "6":
            comprobar_contenido_y_eliminar()
            comprobar_y_crear_carpetas(['./info/','./evidencias/'])
            fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d')
            with open('./info/fecha.txt', 'w') as archivo:
                archivo.write(fecha_actual)
            montaje()
            seleccionar_dispositivo()
            limpiar_pantalla()
        elif opcion == "S":
            salir()
            break
        else:
            print(Fore.RED + "Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    salir()