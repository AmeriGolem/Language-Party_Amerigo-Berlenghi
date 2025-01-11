#!/bin/bash

downloaded_file=""
#from https://stackoverflow.com/questions/1521462/looping-through-the-content-of-a-file-in-bash
cat urls.txt | while read line || [[ -n $line ]];
do
   curl -O $line
   downloaded_file+="  $line"
done

echo "The Downloaded files are: $downloaded_file"

