#!/bin/bash
checkV="\e[32m[-->]\e[0m"
checkR="\e[31m[!!]\e[0m"

#seleccionamos la fecha
start_time=$(head -n 1 ./info/fecha.txt)
disco=$1

#variable para iteración
i=1
echo $disco
echo $start_time

#Comprobamos si tiene particiones
sudo lsblk -l $disco | grep part|awk '{print $1}'|column -t|uniq > ./info/$start_time/particiones.txt

file="./info/$start_time/particiones.txt"
echo $file

# Comprobar si el fichero está vacío
if [ $(stat -c%s "$file") -eq 0 ]; 
then
    echo -e "$checkR: No se encontraron particiones en el disco $disco\e[0m"
    #exit 1
    echo "esto es 1"
    #sleep 20
else
    echo -e "$checkV: Se encontraron particiones en el disco $disco\e[0m"   
    echo "esto es 2"
    #sleep 20
fi