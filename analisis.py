
from colorama import Fore, Style
from utils import obtener_disco_seleccionado, ejecutar_comando, esperar_pulsacion_tecla


def mostrar_informacion_hardware():
    #Muestra información de hardware utilizando comandos de Linux.
    print(Fore.GREEN + Style.BRIGHT + "\nInformación de Hardware:")
    print(Fore.CYAN + "\nInformación de Bloques de Dispositivos:")    
    comand=ejecutar_comando(["./scripts/info_hard.sh", obtener_disco_seleccionado()])
    print(comand)

def mostrar_informacion_software():
    print(Fore.GREEN + Style.BRIGHT + "\nInformación de Software:")
    # Obtener el nombre del sistema operativo
    #sistema_operativo = platform.uname().system
    #print(f"El sistema operativo es: {sistema_operativo}") 
        
    comand=ejecutar_comando(["./scripts/info_soft.sh", obtener_disco_seleccionado()])
    print(comand)

def mostrar_informacion_cifrado():
    
    Luks_info = """
    LUKS1

    Encabezado: Formato específico con una clave maestra cifrada por claves derivadas de contraseñas.
    Ranuras de clave: Hasta 8, permitiendo múltiples contraseñas.
    Algoritmos de cifrado: Soporta varios, incluyendo AES.
    Hash y KDF: Usa SHA-1 y PBKDF2 para fortalecer contraseñas.
    Compatibilidad: Amplia compatibilidad con herramientas Linux.

    LUKS2   

    Encabezado mejorado: Más flexible y extensible para futuras mejoras.
    Ranuras de clave: Soporta más de 8 ranuras.
    KDF mejorado: Utiliza Argon2i y Argon2id, más resistentes a ataques de fuerza bruta.
    Integridad y autenticación: Soporta AEAD para proteger contra la manipulación de datos.
    Metadatos adicionales: Permite almacenar metadatos extra.
    Compatibilidad: Retrocompatible con LUKS1.
    Backup y restauración: Mejoradas.
    Flexibilidad: Mayor elección de algoritmos de cifrado y hash.

    Comparación

    Seguridad: LUKS2 es más seguro gracias a KDFs avanzados y AEAD.
    Flexibilidad: LUKS2 es más adaptable y extensible.
    Compatibilidad: LUKS1 es muy estable y compatible, LUKS2 permite una transición gradual.

    """
    Bitlocker_info = """
    Versiones de BitLocker

    Version 1:
        Significado: Esta es la versión inicial de BitLocker introducida con Windows Vista y Windows Server 2008.
        Características: Soporta cifrado completo de disco utilizando AES con soporte para varios métodos de autenticación como TPM (Trusted Platform Module), PIN, y claves USB.

    Version 2:
        Significado: Introducida con Windows 7 y Windows Server 2008 R2.
        Características: Mejoras en la usabilidad y administración, incluyendo soporte para cifrado en dispositivos de arranque y almacenamiento, y mejor integración con el sistema operativo.

    Version 3:
        Significado: Apareció con Windows 8 y Windows Server 2012.
        Características: Incluye soporte para cifrado de discos duros con cifrado acelerado por hardware, y mejor soporte para discos dinámicos y particiones no estándar.

    Version 4:
        Significado: Introducida con Windows 8.1 y Windows Server 2012 R2.
        Características: Añade soporte para la función "Encrypted Hard Drives" y mejoras en la velocidad de cifrado/desifrado, así como en la administración de claves.

    Version 5:
        Significado: Esta versión se utiliza en Windows 10 y Windows Server 2016 en adelante.
        Características: Incluye soporte mejorado para cifrado en discos SSD y almacenamiento basado en la nube, además de nuevas funcionalidades de administración y políticas de grupo.

    Version 6:
        Significado: Utilizada en versiones más recientes de Windows 10 y Windows 11.
        Características: Introduce mejoras de seguridad adicionales y optimizaciones para nuevas tecnologías de almacenamiento y cifrado.
    """

    # Comprobamos cifrado de particiones
    print(Fore.GREEN + Style.BRIGHT + "\nInformación de Cifra:")
    comand=ejecutar_comando(["./scripts/info_cript.sh", obtener_disco_seleccionado()])
    print(comand)    
    opcion = input(Fore.CYAN + "Para más información sobre el tipo de cifrado pulse B(Bitlocker) - L(LUKS) - F(FileVault) o ENTER para continuar: ")    
    if opcion == "B":
        print(Fore.CYAN + Bitlocker_info)
        esperar_pulsacion_tecla()
    elif opcion == "L":
        print(Fore.CYAN + Luks_info)
        esperar_pulsacion_tecla()

