#!/bin/bash

##Completely empty file
#for f in ./*.txt; do 
#	cat /dev/null > $f
#done

#Remove lines matching holder
for f in ./*.txt; do 
	echo "$f"
	sed -i 's/miaphysite/miaphysitism/' $f
done


