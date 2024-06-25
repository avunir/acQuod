from colorama import Fore, Style
from utils import ejecutar_comando,  listar_particiones, esperar_pulsacion_tecla, limpiar_pantalla
from dependencias import obtener_fecha

def imprimir_hash():
    with open('./evidencias/' + obtener_fecha() + '/hashes.txt', 'r') as file:
        for line in file:
            print(Fore.YELLOW + line)

def calculo_hash(disco):
    #Presenta el menú cálculo de hash
    limpiar_pantalla()
     
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
        print(Fore.CYAN + "\nMenú de copiado y cálculo de hash:")
        print(Fore.CYAN + "1. Proceso automático completo, copiado y cálculo de hashes (md5 y sha256)")
        print(Fore.CYAN + "2. Calcular MD5 y copiar")
        print(Fore.CYAN + "3. Calcular SHA-256 y copiar")
        print(Fore.CYAN + "4. Calcular SHA-512 y copiar")        
        print(Fore.CYAN + "5. Adquirir sin calcular el hash")
        print(Fore.CYAN + "S. Salir")
        print(Fore.YELLOW + Style.BRIGHT + "\nDispositivo seleccionado: " + disco)
        print(Fore.CYAN + "=" * 40 + "\n")

        opc = input(Fore.CYAN + "Selecciona una opción (1-6)(S salir): ")
        print("\n")

        if opc == "1":
            print(Fore.GREEN + "--> Cálculando MD5 y SHA256 de: " + disco)
            with open('./evidencias/' + obtener_fecha() + '/hashes.txt', 'w') as file:
                file.write("####" + disco + "####\n")
            ejecutar_comando(["./scripts/calc_md5.sh", disco])
            ejecutar_comando(["./scripts/calc_sha256.sh", disco])
            imagendd = ("./evidencias/" + obtener_fecha() + disco + ".dd")
            imagenff = imagendd.replace("/dev", "")
            print(Fore.GREEN + "--> Realizando copia de " + disco + " en " + imagenff)
            ejecutar_comando(["./scripts/copia_dd.sh", disco])
            print(Fore.GREEN + "--> Cálculando MD5 y SHA256 de: " + imagenff)
            ejecutar_comando(["./scripts/calc_md5.sh", imagenff])
            ejecutar_comando(["./scripts/calc_sha256.sh", imagenff])
            imprimir_hash()
            esperar_pulsacion_tecla()            
            break

        elif opc == "2":
            print(Fore.GREEN + "--> Cálculando MD5 de: " + disco)
            with open('./evidencias/' + obtener_fecha() + '/hashes.txt', 'w') as file:
                file.write("##" + disco + "##\n")
            ejecutar_comando(["./scripts/calc_md5.sh", disco])
            imagendd = ("./evidencias/" + obtener_fecha() + disco + ".dd")
            imagenff = imagendd.replace("/dev", "")
            print(Fore.GREEN + "--> Realizando copia de " + disco + " en " + imagenff)
            ejecutar_comando(["./scripts/copia_dd.sh", disco])
            print(Fore.GREEN + "--> Cálculando MD5 de: " + imagenff)
            ejecutar_comando(["./scripts/calc_md5.sh", imagenff])
            imprimir_hash()
            esperar_pulsacion_tecla()
            break

        elif opc == "3":
            print(Fore.GREEN + "--> Cálculando SHA256 de: " + disco)
            with open('./evidencias/' + obtener_fecha() + '/hashes.txt', 'w') as file:
                file.write("##" + disco + "##\n")
            ejecutar_comando(["./scripts/calc_sha256.sh", disco])
            imagendd = ("./evidencias/" + obtener_fecha() + disco + ".dd")
            imagenff = imagendd.replace("/dev", "")
            print(Fore.GREEN + "--> Realizando copia de " + disco + " en " + imagenff)
            ejecutar_comando(["./scripts/copia_dd.sh", disco])
            print(Fore.GREEN + "--> Cálculando SHA256 de: " + imagenff)
            ejecutar_comando(["./scripts/calc_sha256.sh", imagenff])
            imprimir_hash()
            esperar_pulsacion_tecla()
            break

        elif opc == "4":
            print(Fore.GREEN + "--> Cálculando SHA512 de: " + disco)
            with open('./evidencias/' + obtener_fecha() + '/hashes.txt', 'w') as file:
                file.write("##" + disco + "##\n")
            ejecutar_comando(["./scripts/calc_sha512.sh", disco])
            imagendd = ("./evidencias/" + obtener_fecha() + disco + ".dd")
            imagenff = imagendd.replace("/dev", "")
            print(Fore.GREEN + "--> Realizando copia de " + disco + " en " + imagenff)
            ejecutar_comando(["./scripts/copia_dd.sh", disco])
            print(Fore.GREEN + "--> Cálculando SHA512 de: " + imagenff)
            ejecutar_comando(["./scripts/calc_sha512.sh", imagenff])
            imprimir_hash()
            esperar_pulsacion_tecla()
            break

        elif opc == "5":
            imagendd = ("./evidencias/" + obtener_fecha() + disco + ".dd")
            imagenff = imagendd.replace("/dev", "")
            print(Fore.GREEN + "--> Realizando copia de " + disco + " en " + imagenff + " ...")
            ejecutar_comando(["./scripts/copia_dd.sh", disco])
            print(Fore.GREEN + "--> Copia finalizada")
            esperar_pulsacion_tecla()
            break
        elif opc == "S":
            break            
        else:
            print(Fore.RED + "Opción no válida. Inténtalo de nuevo.")            

'''def adquirir(opcion):
    print(Fore.GREEN + Style.BRIGHT + "\nInformación de Adquisición: " + opcion)
    comand = ejecutar_comando(["./scripts/calc_hash.sh", opcion])
    print(comand)'''

def adquirir_particiones():
    #Leemos el dispositivo seleccionado
    try:
        with open('./info/' + obtener_fecha() + '/disco_seleccionado.txt', 'r') as f:
            dispositivo = f.readline().strip()
    except FileNotFoundError:
        print(f"Error: El fichero {'./info/' + obtener_fecha() + '/disco_seleccionado.txt'} no existe.")
    except Exception as e:
        print(f"Error al leer el fichero {'./info/' + obtener_fecha() + '/disco_seleccionado.txt'}: {e}")
    
    particiones = listar_particiones(dispositivo)
    
    print("\nSeleccione una partición o el disco completo para ADQUIRIR:")

    # Iteramos sobre la lista de líneas y mostrar el número de línea y el contenido
    for i, linea in enumerate(particiones, 1):        
        dsistema = ejecutar_comando(['./scripts/disco_sistema.sh', str(linea)])        
        dsize = ejecutar_comando(["./scripts/disk_size.sh", linea])
        if dsistema != None:
            print(f"{i}. {linea} " + "(Disco del Sistema) " + str(dsize))
        else:
            print(f"{i}. {linea} " + str(dsize))

    opcion = input(Fore.YELLOW + Style.BRIGHT + "Seleccione una opción para ADQUIRIR: ")
    # Validar la entrada del usuario
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(particiones):
        print("Opción no válida. Por favor, ingrese un número válido.")
        opcion = input("Ingrese el número de la opción que desea seleccionar: ")

    # Obtener el contenido correspondiente a la opción seleccionada    
    dispositivo_seleccionado = particiones[int(opcion) - 1]
    print(Fore.GREEN + Style.BRIGHT + "\nOpción seleccionada: " + str(dispositivo_seleccionado))
    calculo_hash(dispositivo_seleccionado)

if __name__ == "__main__":
    adquirir_particiones()