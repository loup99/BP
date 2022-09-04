@echo off

pandoc.exe "--columns=250" "-c" "pandoc.css" "-f" "mediawiki" "-t" "html5" "-s" "Faith.wiki" "-o" "Faith.html"
pandoc.exe "--columns=250" "-c" "pandoc.css" "-f" "mediawiki" "-t" "html5" "-s" "Differences.wiki" "-o" "Differences.html"
pandoc.exe "--columns=250" "-c" "pandoc.css" "-f" "mediawiki" "-t" "html5" "-s" "Historical_Notes.wiki" "-o" "Historical_Notes.html"
pandoc.exe "--columns=250" "-c" "pandoc.css" "-f" "mediawiki" "-t" "html5" "-s" "Main_Page.wiki" "-o" "Main_Page.html"

python3 "_merge_faith_table_cells.py"
python3 "_color_faith_table_cells.py"
pause