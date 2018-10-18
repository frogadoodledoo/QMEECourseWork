#!/bin/bash

for f in *.pdf; 
    do  
        echo "Converting $f"; 
        convert "$f"  "$(basename "$f" .pdf).png"; 
    done

