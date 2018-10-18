#!/bin/bash
# Author: Merry Crowson
# Script: csvtospace.sh
# Desc: substitute the commas in the files with spaces
#
# saves the output into a .txt file
# Arguments: 1-> tab delimited file
# Date: Oct 2018



filename=$(basename $1)
dirname=$(dirname $1)
filename="${filename%.*}" # strips the extension


cat $1 | tr -s "," " " > "${dirname}/${filename}.txt";
 

echo "Done!"
