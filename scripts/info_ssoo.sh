#!/bin/bash


MOUNT_POINT="/mnt/forense_1"

# Función para detectar sistema basado en Linux
check_linux() {
    if [ -f "$MOUNT_POINT/etc/os-release" ]; then
        echo "Linux"
        cat "$MOUNT_POINT/etc/os-release"
        return 0
    elif [ -f "$MOUNT_POINT/etc/issue" ]; then
        echo "Linux"
        cat "$MOUNT_POINT/etc/issue"
        return 0
    fi
    return 1
}

# Función para detectar sistema basado en Windows
check_windows() {
    if [ -d "$MOUNT_POINT/Windows/System32" ]; then
        echo "Windows"
        return 0
    fi
    return 1
}

# Función para detectar sistema basado en macOS
check_macos() {
    if [ -d "$MOUNT_POINT/System/Library/CoreServices" ]; then
        echo "macOS"
        return 0
    fi
    return 1
}

# Ejecutar las funciones de detección
if check_linux; then
    exit 0
elif check_windows; then
    exit 0
elif check_macos; then
    exit 0
else
    echo "Sistema operativo no detectado"
    exit 1
fi
