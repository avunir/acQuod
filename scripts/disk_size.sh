#!/bin/bash
echo "$(sudo lsblk -o SIZE $1 | grep -v SIZE | head -n 1 |  tr -d ' ')"


