#!/bin/bash
checkV="\e[32m[-->]\e[0m"
checkR="\e[31m[!!]\e[0m"

disco=$1

#seleccionamos la fecha
start_time=$(head -n 1 ./info/fecha.txt)
i=1

sudo lsblk -l $disco | grep part|awk '{print $1}'|column -t|uniq > ./info/$start_time/particiones.txt
while read linea
do
    cadena=$(sudo mount | grep -i "/dev/$linea")
    retval=$?

    if [ $retval -eq 1 ];
    then
        sudo mkdir /mnt/forense_$i > /dev/null 2>&1        
        sudo mount /dev/$linea /mnt/forense_$i > /dev/null 2>&1
        # Verificar si el comando tuvo éxito o no
        if [ $? -eq 0 ]; then
            echo -e "\e[32mINFORMACIÓN DE LA PARTICIÓN: $linea \e[0m\n"
            echo -e "$checkV Partición $linea montada en SOLO LECTURA"
            echo -e "$checkV Contenido de la partición: " 
            sudo ls -lah /mnt/forense_$i
            echo -e "$checkV $(sudo df -hT /mnt/forense_$i)"
        else
            echo -e "\e[32mINFORMACIÓN DE LA PARTICIÓN: $linea \e[0m\n"
            echo -e "$checkR No se pudo montar la partición $linea"
        fi        
    fi    
   
    echo -e "$checkV $(sudo lsblk -f /dev/$linea)"
    echo -e "$checkV $(sudo partx -s /dev/$linea)"
    #echo -e ""
    
    ((i++))
    echo "$i"

done < ./info/$start_time/particiones.txt

sudo umount /mnt/forense_* > /dev/null 2>&1
sudo rmdir /mnt/forense_* > /dev/null 2>&1