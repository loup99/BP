import os
import re
import sys

#Tool for changing years foward or backwards throught a mod. To be run in the top level folder
#(containing common/, events/ &c.). Excludes stuff in gfx/, gui/, map_data/ directories.

date_increment = 999

the_date_pattern = '([0-9]{3})\.([0-9]{1,2}).([0-9]{1,2})'

for dirpath, dirnames, filenames in os.walk("."):
    dirnames = [the_dir for the_dir in dirnames if the_dir not in ['gfx','gui','map_data']]
    for filename in [f for f in filenames if f.endswith(".txt")]:
        input_file_name = os.path.join(dirpath,filename)
        output_file_name = os.path.join(dirpath,'tmp.txt')
        print(input_file_name)
        with open(input_file_name,'r') as fid:
            input_text = fid.readlines()
        index = -1
        has_dates = False
        for line in input_text:
            index+=1
            match = re.search(the_date_pattern,line)
            if ( match ):
                has_dates = True
                groups = match.groups()
                year = groups[0]
                new_year = str(int(year)+date_increment)
                repl = new_year+'.'+groups[1]+'.'+groups[2]
                new_line = re.sub(the_date_pattern,repl,line)
                input_text[index] = new_line
        if ( has_dates ):
            with open(output_file_name,'w') as fid:
                fid.writelines(input_text)
            os.system('mv '+output_file_name+' '+input_file_name)