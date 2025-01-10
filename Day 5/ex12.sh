#!/bin/bash

for i in {1..3}
do
touch "ex$i.py"
echo {'print("Hello from ex'$i'.py")'} > ex$i.py
echo "ex$i.py créé"
done