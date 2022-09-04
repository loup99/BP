#Faith
pandoc.exe -c pandoc.css -f mediawiki -t html5 -s Faith.wiki -o Faith.html

#NB: Merge *before* coloring to avoid having the parser fail

#Merge Table Cells
python3 _merge_faith_table_cells.py

#Color Table Cells
python3 _color_faith_table_cells.py

