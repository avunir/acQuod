#!/bin/bash

#seleccionamos la fecha
start_time=$(head -n 1 ./info/fecha.txt)
#creamos directorios necesarios
mkdir ./info/$start_time
#echo $start_time > ./info/fecha.txt
#Discos conectados
#sudo lsblk -p | grep -v loop |grep -i disk
sudo lsblk -p | grep -v loop |grep -i disk > ./info/$start_time/discos_conectados.txt
