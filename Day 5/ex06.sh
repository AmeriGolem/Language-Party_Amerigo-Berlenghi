#!/bin/bash

file=test.txt
if [ -e "$file" ]
then
    echo "Le fichier existe."
else
    echo "Le fichier n'existe pas."
fi