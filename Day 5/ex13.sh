#!/bin/bash

used=$(df --total --output=pcent / | tail -n1 | tr -d '%')
if [ "$used" -gt 90 ]
then
    echo "Il y a moins de 10% d'espace de stockage!"
else
    echo "tout va bien"
fi