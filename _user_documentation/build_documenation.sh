#Faith
pandoc.exe --columns=250 -c pandoc.css -f mediawiki -t html5 -s Faith.wiki -o Faith.html
pandoc.exe --columns=250 -c pandoc.css -f mediawiki -t html5 -s Culture.wiki -o Culture.html
pandoc.exe --columns=250 -c pandoc.css -f mediawiki -t html5 -s Traditions.wiki -o Traditions.html
pandoc.exe --columns=250 -c pandoc.css -f mediawiki -t html5 -s Differences.wiki -o Differences.html
pandoc.exe --columns=250 -c pandoc.css -f mediawiki -t html5 -s Historical_Notes.wiki -o Historical_Notes.html
pandoc.exe --columns=250 -c pandoc.css -f mediawiki -t html5 -s Main_Page.wiki -o Main_Page.html

#NB: Merge *before* coloring to avoid having the parser fail

#Merge Table Cells
python3 _merge_table_cells.py

#Color Table Cells
python3 _color_table_cells.py

#Some additional cleanup
python3 _remove_trailing_terms.py
