#!/bin/bash

tar -cvf mon_archive.tar.gz *.txt

mkdir extraction

tar -xf mon_archive.tar.gz -C extraction
