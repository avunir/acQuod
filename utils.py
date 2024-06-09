import subprocess
import os,sys

from colorama import init, Fore, Style

# Definición de funciones

#Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('clear')

# Obtener la fecha y hora actual
def obtener_fecha():
    with open('./info/fecha.txt', 'r') as archivo:
        fecha_actual = archivo.readline()
    return str(fecha_actual)

#Función para seleccionar el dispositivo por parte del usuario
def seleccionar_dispositivo():
    dispositivos_conectados = []
    ejecutar_script_linux("./scripts/discos_conectados.sh")    
    print(Fore.GREEN + Style.BRIGHT + "\n=============================================================\n")
    print(Fore.GREEN + Style.BRIGHT + "\nCONECTE el dispopsitivo de almacenamiento que quiera analizar\n")
    print(Fore.GREEN + Style.BRIGHT + "\n=============================================================\n")
    esperar_pulsacion_tecla()
    with open('./info/' + obtener_fecha() + '/discos_conectados.txt', 'r') as file:
        for line in file:
            dispositivos_conectados.append(line.strip().split()[0])
    
    # Mostrar el menú dinámico
    """ Listamos los discos conectados"""
    print(Fore.YELLOW + Style.BRIGHT + "\nDiscos Conectados al sistema")
    print("Seleccione un dispositivo para analizar:")
    #for i, linea in enumerate(dispositivos_conectados, 1):
    #    print(f"{i}. {linea}")

    # Iterar sobre la lista de líneas y mostrar el número de línea y el contenido
    for i, linea in enumerate(dispositivos_conectados, 1):        
        dsistema = ejecutar_comando(['./scripts/disco_sistema.sh', str(linea)])        
        dsize = ejecutar_comando(["./scripts/disk_size.sh", linea])
        
        
        
        if dsistema != None:
            print(f"{i}. {linea} " + "(Disco del Sistema) " + str(dsize))
        else:
            print(f"{i}. {linea} " + str(dsize))
    
        
    opcion = input(Fore.YELLOW + Style.BRIGHT + "Seleccione un dispositivo para analizar: ")    
    # Validar la entrada del usuario
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(dispositivos_conectados):
        print("Opción no válida. Por favor, ingrese un número válido.")
        opcion = input("Ingrese el número de la opción que desea seleccionar: ")

    # Obtener el contenido correspondiente a la opción seleccionada
    
    dispositivo_seleccionado = dispositivos_conectados[int(opcion) - 1]
    with open('./info/' + str(obtener_fecha()) + '/disco_seleccionado.txt', 'w') as file:
        file.write(dispositivo_seleccionado)

    limpiar_pantalla()    
    
    return dispositivo_seleccionado

# Obtener dispositivo seleccionado por el usuario
def obtener_disco_seleccionado():
    with open('./info/' + obtener_fecha() + '/disco_seleccionado.txt', 'r') as file:
        dispositivo = file.readline()
    return str(dispositivo)

#Funcion para esperar pulsación de tecla
def esperar_pulsacion_tecla():
    """
    Espera una pulsación de tecla.
    """    
    import termios
    import tty
    print(Fore.LIGHTGREEN_EX + "Presiona cualquier tecla para continuar...")
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

#Función para ejecutar un comando en la terminal
def ejecutar_comando(comando):
    """
    Ejecuta un comando en la terminal y devuelve su salida.
    
    :param comando: Lista que contiene el comando y sus argumentos.
    :return: Salida del comando como una cadena de texto.
    """
    try:
        resultado = subprocess.run(comando, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if resultado.stdout != '\n':
            return resultado.stdout
    except subprocess.CalledProcessError as e:
        #return f"Error al ejecutar {comando}: {e.stderr}"
        return None

#función para ejecutar un script Bash
def ejecutar_script_linux(ruta_script):
    """
    Ejecuta un script de shell desde Python.

    Args:
        ruta_script (str): La ruta al script de shell que se ejecutará.
    """
    try:
        resultado = subprocess.run([ruta_script], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f" \n{resultado.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el script: {e.stderr}")

def adquirir_dispositivos():
    # Función ficticia para el ejemplo
    print(Fore.GREEN + "Adquiriendo dispositivos...")

