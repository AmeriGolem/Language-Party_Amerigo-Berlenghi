#!/bin/bash
mkdir backup

for f in *.txt
do
    cp $f backup/$f
done
