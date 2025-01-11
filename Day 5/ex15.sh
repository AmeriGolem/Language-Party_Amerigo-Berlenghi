#!/bin/bash

for doc in *.tmp
do
    if [ -e $doc ]
    then
        rm $doc
        echo "remmoved $doc"
    else
        echo "there are no .tmp files"
    fi
done

if [ -e *.log ]
then
    tar -cvf mon_archive.tar.gz *.log
    rm *.log
    echo "Les fichiers log on été archivé"
else
    echo "Il n'y a pas de fichier .log"
fi