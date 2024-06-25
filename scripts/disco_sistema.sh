#!/bin/bash
echo "$(sudo mount | grep "$1" | grep -E '(^| )/( |$)')"

