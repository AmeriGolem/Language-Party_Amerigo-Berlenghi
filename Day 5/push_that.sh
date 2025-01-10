#!/bin/bash
if [ "git rev-parse --is-inside-work-tree" ] && [[ $1 != "" ]]
then
    git add *
    git commit -m $1
    git push

else
    echo parameter 1 missing
fi