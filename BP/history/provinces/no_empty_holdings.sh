#!/bin/bash

#Remove lines matching holder

#depression and lunacy assumed to be **not** genetic
for f in ./*.txt; do 
	echo "$f"
	sed -i 's/holding[ ]*=[ ]*none/holding = castle_holding/g' $f
done
unix2dos *.txt
