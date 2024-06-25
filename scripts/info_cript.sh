#!/bin/bash

#Colores
checkV="\e[32m[**]\e[0m"
checkR="\e[31m[!!]\e[0m"

#seleccionamos la fecha
start_time=$(head -n 1 ./info/fecha.txt)

disco=$1

##Buscamos cabeceras de cifrado en las particiones
sudo lsblk -l $disco | grep part|awk '{print $1}'|column -t|uniq > ./info/$start_time/particiones.txt
while read linea
do
    echo -e ""
    echo -e "$checkV Mostrando información de la particion: /dev/$linea"

    #COMPROBAMOS BITLOCKER    
    cadena=$(sudo hexdump -n 10485760 -C /dev/$linea |grep -i "fve-")
    retval=$? 
    if [ $retval -eq 0 ];
    then
        echo -e "$checkR IDENTIFICADA PARTICIÓN CIFRADA CON BITLOCKER"
        sudo dislocker-metadata -V /dev/$linea > ./info/$start_time/cifra_identificada.txt
        sudo dislocker-metadata -V /dev/$linea | grep -e Signature -e Version -e VMK -e PK -e state -e Encryption -e Recovery
        continue
    fi 
    #echo -e "" 
   
    cadena=$(sudo xxd -l 0x00900000 /dev/$linea |grep "3bd6 6749 292e d84a 8399 f6a3 39e3 d0")
    retval=$?    
    if [ $retval -eq 0 ];
    then
        echo -e "$checkR IDENTIFICADA PARTICIÓN CIFRADA CON BITLOCKER"
        sudo xxd -l xxd -s 0x008bc000 -l 0x30 /dev/$linea > ./info/$start_time/cifra_identificada.txt
        sudo xxd -l xxd -s 0x008bc000 -l 0x30 /dev/$linea
        continue
    fi
    #echo -e ""

    #COMPROBAMOS FILEVAULT
    cadena=$(sudo hexdump -n 10485760 -C /dev/$linea |grep -i "encrdsa")
    retval=$?
    if [ $retval -eq 0 ];
    then
        echo -e "$checkR IDENTIFICADA PARTICIÓN CIFRADA CON FILEVAULT"
        sudo hexdump -n 10485760 -C /dev/$linea |grep -i "encrdsa" > ./info/$start_time/cifra_identificada.txt
        sudo hexdump -n 10485760 -C /dev/$linea |grep -i "encrdsa"
        continue
    fi
    #echo -e "" 

    #COMPROBAMOS LUKS
    cadena=$(sudo xxd -l 0x60 /dev/$linea | grep "4c55 4b53 babe")
    retval=$?
    if [ $retval -eq 0 ];
    then
        echo -e "$checkR IDENTIFICADA PARTICIÓN CIFRADA CON LUKS"
        #sudo xxd -l 0x60 /dev/$linea
        echo -e ""
        sudo cryptsetup luksDump /dev/$linea > ./info/$start_time/cifra_identificada.txt
        sudo cryptsetup luksDump /dev/$linea
        continue
    fi
    #echo -e ""
    
done < ./info/$start_time/particiones.txt