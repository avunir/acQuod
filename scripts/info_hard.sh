#!/bin/bash

#seleccionamos la fecha
start_time=$(head -n 1 ./info/fecha.txt)

disco=$1
#Ejecutamos comandos lsblk y blkid para obtener información de la partición

sudo lsblk $disco -o NAME,FSTYPE,SIZE,MOUNTPOINT -lp |grep -v loop | grep -v NAME > ./info/$start_time/lsblk.txt 2>&1
sudo lsblk $disco -o NAME,FSTYPE,SIZE,MOUNTPOINT -lp |grep -v loop | grep -v NAME

echo -e ""
sudo blkid -i $disco > ./info/$start_time/blkid.txt 2>&1
sudo blkid -i $disco
