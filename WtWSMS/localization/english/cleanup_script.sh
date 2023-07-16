#!/usr/bin/bash
array=()
for item in "${array[@]}"
do
	echo "$item"
	sed -i "/$item/d" BP_titles_l_english.yml
	#sed -i "/$item/d" $(find ./dynasties -iname "*.yml")
done
