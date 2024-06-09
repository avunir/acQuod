from colorama import init, Fore, Style
import subprocess

def obtener_estado_automontaje():
    try:
        estado_automontaje = subprocess.run(
            ['gsettings', 'get', 'org.gnome.desktop.media-handling', 'automount'],
            capture_output=True,
            text=True,
            check=True
        ).stdout.strip()

        estado_automontaje_open = subprocess.run(
            ['gsettings', 'get', 'org.gnome.desktop.media-handling', 'automount-open'],
            capture_output=True,
            text=True,
            check=True
        ).stdout.strip()
        
        return estado_automontaje, estado_automontaje_open
    except subprocess.CalledProcessError as e:
        print(f"Error al obtener el estado del automontaje: {e}")
        return None, None

def cambiar_estado_automontaje(estado):
    try:
        subprocess.run(['gsettings', 'set', 'org.gnome.desktop.media-handling', 'automount', estado], check=True)
        subprocess.run(['gsettings', 'set', 'org.gnome.desktop.media-handling', 'automount-open', estado], check=True)
        print(f"Automontaje de dispositivos externos {'habilitado' if estado == 'true' else 'deshabilitado'} en GNOME.")
    except subprocess.CalledProcessError as e:
        print(f"Error al cambiar el estado del automontaje: {e}")

def montaje():
    estado_automontaje, estado_automontaje_open = obtener_estado_automontaje()
        
    if estado_automontaje == "false" and estado_automontaje_open == "false":
        return

    print(f"Estado actual del automontaje: {estado_automontaje} y {estado_automontaje_open}")

    accion = input("¿Desea habilitar (h) o deshabilitar (d) el automontaje de dispositivos externos? (h/d): ").strip().lower()

    if accion == 'h':
        cambiar_estado_automontaje('true')
    elif accion == 'd':
        cambiar_estado_automontaje('false')
        print(Fore.YELLOW + Style.BRIGHT + "Es necesario reiniciar GNOME para que se aplique el cambio.")
    else:
        print("Acción no reconocida. Por favor, introduzca 'h' para habilitar o 'd' para deshabilitar.")

if __name__ == "__main__":
    montaje()
