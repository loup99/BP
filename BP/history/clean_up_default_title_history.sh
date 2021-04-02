#!/bin/bash

##Completely empty file
#for f in ./*.txt; do 
#	cat /dev/null > $f
#done

#Remove lines matching holder
for f in ./*.txt; do 
	echo "$f"
	sed -i '/holder = /d' $f
done
for f in ./*.txt; do 
	echo "$f"
	sed -i '/holder=/d' $f
done

#Remove lines matching holder
for f in ./*.txt; do 
	echo "$f"
	sed -i '/liege = /d' $f
done
for f in ./*.txt; do 
	echo "$f"
	sed -i '/liege=/d' $f
done

#Remove lines matching government
for f in ./*.txt; do 
	echo "$f"
	sed -i '/government = /d' $f
done

#Remove lines matching numbers
for f in ./*.txt; do 
	echo "$f"
	sed -i '/[0-9] = /d' $f
done
for f in ./*.txt; do 
	echo "$f"
	sed -i '/[0-9]=/d' $f
done

#Remove lines matching set_capital_county
for f in ./*.txt; do 
	echo "$f"
	sed -i '/set_capital_county = /d' $f
done

#Remove lines matching effect
for f in ./*.txt; do 
	echo "$f"
	sed -i '/effect = /d' $f
done

#Remove lines matching change_development_level
for f in ./*.txt; do 
	echo "$f"
	sed -i '/change_development_level/d' $f
done

Remove lines matching insert_title_history
for f in ./*.txt; do 
	echo "$f"
	sed -i '/insert_title_history/d' $f
done

#Remove lines matching name =
for f in ./*.txt; do 
	echo "$f"
	sed -i '/name = /d' $f
done

#Remove lines matching add_to_global_variable_list =
for f in ./*.txt; do 
	echo "$f"
	sed -i '/add_to_global_variable_list = /d' $f
done

Remove lines matching flag:
for f in ./*.txt; do 
	echo "$f"
	sed -i '/flag\:/d' $f
done

#Remove lines matching comments
for f in ./*.txt; do 
	echo "$f"
	sed -i '/\#/d' $f
done

#Remove lines matching close brackets
for f in ./*.txt; do 
	echo "$f"
	sed -i '/\}/d' $f
done

#Remove multiple blank lines
for f in ./*.txt; do 
	echo "$f"
	sed -i '/^[[:space:]]*$/d' $f
done

#close brackets
for f in ./*.txt; do 
	echo "$f"
	sed -i 's/$/\}/' $f
done





