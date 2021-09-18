#! /bin/bash

if [ "$#" -eq 1 ]
then
    file="$1"
    python3 main.py "$file"
elif [ "$#" -gt 1 ]
then
    echo "Arguments must be single input file."
    exit 1
else
    echo "Please provied input file."
    exit 1
fi