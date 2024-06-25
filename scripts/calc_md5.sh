#!/bin/bash
checkV="\e[32m[-->]\e[0m"

#seleccionamos la fecha
start_time=$(head -n 1 ./info/fecha.txt)

#Creamos directorio
mkdir ./evidencias/$start_time/ 2>/dev/null
#particiones=$(head ./info/$start_time/particiones.txt)
disco=$1
echo "$disco"

echo -e "$checkV Calculando MD5 de $disco, esto puede tardar un tiempo según el tamaño"            
#echo "Tipo de Hash: MD5" >> "./evidencias/$start_time/hashes.txt" 
echo "Hash MD5: $(sudo md5sum "$disco")" >> "./evidencias/$start_time/hashes.txt"            
#echo " " >> "./evidencias/$start_time/hashes.txt" 