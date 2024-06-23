#!/bin/bash
checkV="\e[32m[-->]\e[0m"

#seleccionamos la fecha
start_time=$(head -n 1 ./info/fecha.txt)

#Creamos directorio
mkdir ./evidencias/$start_time 2>/dev/null
#particiones=$(head ./info/$start_time/particiones.txt)
disco=$1
fichero=$(echo "$disco" | sed 's|/dev/||')

echo -e "$checkV Realizando copia de $disco..."            
sudo ddrescue $disco "./evidencias/$start_time/$fichero.dd" #"./evidencias/$start_time/$disco.log"
#./scripts/calc_md5.sh "./evidencias/$start_time/$fichero.dd"
