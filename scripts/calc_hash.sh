#!/bin/bash
checkV="\e[32m[-->]\e[0m"
checkR="\e[31m[!!]\e[0m"

#seleccionamos la fecha
start_time=$(head -n 1 ./info/fecha.txt)

#Creamos directorio
mkdir ./evidencias/$start_time/ 2>/dev/null
#particiones=$(head ./info/$start_time/particiones.txt)
disco=$1
echo "$disco"

# Menú principal
function mostrar_menu() {
    echo "Seleccione una opción:"
    echo "1. Calcular MD5"
    echo "2. Calcular SHA-256"
    echo "3. Calcular SHA-512"
    echo "4. Calcular todos"
    echo "S. Salir"
}

# Loop principal del menú
while true; do
    mostrar_menu
    read -p "Selecciona una opción: " eleccion
    case $eleccion in
        1)
            echo -e "$checkV Calculando MD5 de $disco, esto puede tardar un tiempo según el tamaño"            
            sudo echo "Tipo de Hash: MD5" >> "./evidencias/$start_time/hashes.txt" 
            sudo echo "Hash: $(sudo md5sum "$disco" | dialog --gauge "Calculando" 6 30 0)" >> "./evidencias/$start_time/hashes.txt"             
            sudo echo " " >> "./evidencias/$start_time/hashes.txt" 
            ;;
        2)
            echo -e "$checkV Calculando SHA-256 de $disco..."            
            sudo echo "Tipo de Hash: SHA-256" >> "./evidencias/$start_time/hashes.txt" 
            sudo echo "Hash: $(sudo sha256sum "$disco")" >> "./evidencias/$start_time/hashes.txt"             
            sudo echo " " >> "./evidencias/$start_time/hashes.txt" 
            ;;
        3)
            echo -e "$checkV Calculando SHA-512 de $disco..."            
            sudo echo "Tipo de Hash: SHA-512" >> "./evidencias/$start_time/hashes.txt" 
            sudo echo "Hash: $(sudo sha512sum "$disco")" >> "./evidencias/$start_time/hashes.txt"             
            sudo echo " " >> "./evidencias/$start_time/hashes.txt" 
            ;;
        4)
            read -p "Ingrese la ruta de la imagen dd: " ruta_imagen
            read -p "Ingrese la ruta del fichero donde guardar los hashes: " fichero
            calcular_todos "$ruta_imagen" | tee -a "$fichero"
            ;;
        S)
            echo "Saliendo..."
            exit 0
            ;;
        *)
            echo "Opción no válida. Intente de nuevo."
            ;;
    esac
done