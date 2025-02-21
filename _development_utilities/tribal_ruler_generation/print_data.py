from .data_types import *

def print_character_history(character_history,religion,fname):
    with open(fname,'w') as file:
        for character in character_history:
            file.write(character.id_num+' = {\n')
            file.write('\tname = '+character.name+'\n')
            file.write('\tdynasty = '+character.dynasty+'\n')
            file.write('\treligion = '+religion+'\n')
            file.write('\tculture = '+character.culture+'\n')
            file.write('\t'+str(character.birth)+'.1.1 = { birth = yes }\n')
            file.write('\t'+str(character.death)+'.1.1 = { death = yes }\n')
            file.write('}\n')

def print_title_history(title_name,title_history,fname,add_government=False):
    with open(fname,'w') as file:
        file.write(title_name+' = {\n')
        for holder,list_loc in zip(title_history,range(len(title_history))):
            if (list_loc == 0) and add_government:
                file.write('\t'+str(holder.accession_date)+'.1.1 = {\n')
                file.write('\t\tholder = '+holder.id_num+'\n')
                file.write('\t\tgovernment = '+holder.government+'\n')
                file.write('\t}\n')
            else:
                file.write('\t'+str(holder.accession_date)+'.1.1 = { holder = '+str(holder.id_num)+ ' }\n')
        file.write('}\n')

def print_dynasty(dynasty,fname):
    with open(fname,'w') as file:
        file.write(dynasty.id_num+' = {\n')
        file.write('\tname = '+dynasty.name+'\n')
        file.write('\tculture = '+dynasty.culture+'\n')
        file.write('}\n')