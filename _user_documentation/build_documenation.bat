@echo off

pandoc.exe "--columns=250" "-c" "pandoc.css" "-f" "mediawiki" "-t" "html5" "-s" "Faith.wiki" "-o" "Faith.html"
python3 "_merge_faith_table_cells.py"
python3 "_color_faith_table_cells.py"
pause