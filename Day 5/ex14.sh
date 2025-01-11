#!/bin/bash
for doc in *.txt
do
    mv $doc "old_$doc"
done