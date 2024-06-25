#!/bin/bash

checkV="\e[34m[**]\e[0m"
checkR="\e[31m[!!]\e[0m"

#seleccionamos la fecha
start_time=$(head -n 1 ./info/fecha.txt)
disco=$1

# Función para identificar el sistema operativo
function identify_os() {
    #local partition=$1
    #mount $partition $mount_point
    mount_point=$1
    
    if [ -f "$mount_point/Windows/System32/kernel32.dll" ]; then
        version=$(grep -oP '(?<=ProductName\s=\s).*(?=\n)' "$mount_point/Windows/System32/license.rtf" | head -1)        
        echo -e "$checkV Sistema Operativo Windows versión $version"
    elif [ -f "$mount_point/etc/fstab" ] && grep -q "Ubuntu" "$mount_point/etc/os-release"; then
        version=$(cat $mount_point/etc/issue)
        echo -e "$checkV Sistema Operativo Linux versión $version"
    elif [ -f "$mount_point/System/Library/CoreServices/SystemVersion.plist" ]; then
        echo -e "$checkV Sistema Operativo MacOS"
    else
        echo -e "$checkR No contiene Sistema Operativo o es desconocido"
    fi
    
    #umount $mount_point
}

#variable para iteración
i=1

#Comprobamos si tiene particiones
sudo lsblk -l $disco | grep part|awk '{print $1}'|column -t|uniq > ./info/$start_time/particiones.txt

#Leemos las particiones y recorremos cada una de ellas
while read linea
do
    #Damos valor para retval
    pmontado=$(sudo mount | grep -i "/dev/$linea")
    retval=$?
    #Si NO está montada
    if [ $retval -eq 1 ];
    then        
        sudo mkdir /mnt/forense_$i > /dev/null 2>&1
        sudo mount -o ro "/dev/$linea" "/mnt/forense_$i" 2>/dev/null
        # Verificar si el comando tuvo éxito o no
        if [ $? -eq 0 ]; then
            echo -e "\n"
            echo -e "\e[32mINFORMACIÓN DE LA PARTICIÓN: $linea \e[0m\n"
            echo -e "$checkV Partición $linea montada en SOLO LECTURA"

            #Identificamos SSOO
            identify_os "/mnt/forense_$i"

            echo -e "$checkV Contenido de la partición: " 
            echo -e "$(sudo ls -lah /mnt/forense_$i)"
            echo -e "$checkV Tamaño y uso de la partición: "
            echo -e "$(sudo df -hT /mnt/forense_$i)"
        else
            echo -e "\n"
            echo -e "\e[32mINFORMACIÓN DE LA PARTICIÓN: $linea \e[0m\n"
            echo -e "$checkR No se pudo montar la partición $linea"
        fi
    #Ya está montada
    else
        pmontado=$(sudo sudo mount | grep -i "/dev/$linea" | cut -d' ' -f3)
        echo -e "\n"
        echo -e "\e[32mINFORMACIÓN DE LA PARTICIÓN: $linea \e[0m\n"
        echo -e "$checkV Partición $linea ya montada previamente"

        #Identificamos SSOO
        identify_os $pmontado
        
        echo -e "$checkV Contenido de la partición: " 
        echo -e "$(sudo ls -lah $pmontado)"
        echo -e "$checkV Tamaño y uso de la partición: "
        echo -e "$(sudo df -hT $pmontado)"
    fi 
    echo -e "$checkV Características de la partición: "
    echo -e "$(sudo lsblk /dev/$linea)"
    sudo lsblk /dev/$linea > ./info/$start_time/lsblk.txt
    echo -e "$checkV Identificación de la partición: "
    echo -e "$(sudo partx -s /dev/$linea)"
    sudo partx -s /dev/$linea > ./info/$start_time/partx.txt
    
    ((i++))

done < ./info/$start_time/particiones.txt
#Desmontamos y eliminamos carpetas creadas
sudo umount /mnt/forense_* > /dev/null 2>&1
sudo rmdir /mnt/forense_* > /dev/null 2>&1

