#!/bin/bash

#seleccionamos la fecha
start_time=$(head -n 1 ./info/fecha.txt)
# Nombre del fichero base
base_name="lsblk.txt"

disco=$1

# Comprobar si el fichero existe
if [ -e "./info/$start_time/$base_name" ]; then
    # Si el fichero existe, encontrar un nuevo nombre
    count=1
    new_name="${base_name%.*}_$count.${base_name##*.}"
    while [ -e "$new_name" ]; do
        count=$((count + 1))
        new_name="${base_name%.*}_$count.${base_name##*.}"
    done
    
    # Crear el nuevo fichero
    touch "./info/$start_time/$new_name"
    #echo "Se ha creado el fichero: $new_name"
    sudo lsblk $disco -o NAME,FSTYPE,SIZE,MOUNTPOINT -lp |grep -v loop | grep -v NAME > ./info/$start_time/$new_name
    sudo lsblk $disco -o NAME,FSTYPE,SIZE,MOUNTPOINT -lp |grep -v loop | grep -v NAME
else
    #echo "El fichero $base_name no existe."
    sudo lsblk $disco -o NAME,FSTYPE,SIZE,MOUNTPOINT -lp |grep -v loop | grep -v NAME > ./info/$start_time/$base_name
    sudo lsblk $disco -o NAME,FSTYPE,SIZE,MOUNTPOINT -lp |grep -v loop | grep -v NAME
fi
echo -e ""
echo -e "$(sudo blkid -i $disco)"
echo -e "$(sudo blkid -d $disco)"


#echo $start_time
#echo $new_name
