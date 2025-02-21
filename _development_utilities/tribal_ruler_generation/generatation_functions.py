from numpy import random as rand
from .data_types import *

random_select = lambda the_list: rand.randint(0,len(the_list))
random_birth_offset = lambda: round(rand.normal(22.0,scale=3.5))

#Wrapper for randomly generating a dynasty, given a culture
def makeDynasty(culture):
    name = culture.dynasty_name_list[random_select(culture.dynasty_name_list)]
    return Dynasty(name,culture.name)

#Wrapper for making a holder, because Python only likes a single constructor
def makeHolder(family,birth,death,name,id_num=0,father=None):
    return Holder(family.culture.name,
                  family.dynasty.name,
                  family.religion,
                  birth,
                  death,
                  name,
                  id_num,
                  father)

#Generates a single character
def generate_char(birth_year,family,id_num=0):
    name = family.culture.male_name_list[random_select(family.culture.male_name_list)]
    death_year = round(rand.normal(loc=birth_year+40,scale=16.0))
    return makeHolder(family,birth_year,death_year,name,id_num,None)

def generate_holders(base_str,culture,religion,start_year,stop_year,start_id_num=0):
    #Build the family
    dynasty = makeDynasty(culture)
    family = Family(culture,dynasty,religion)
    #Initialize the holder list
    holder_list = []
    id_num = start_id_num
    #Initial loop variables
    birth_year = start_year - random_birth_offset()
    end_year = start_year
    #Actually generate holders
    while end_year <= stop_year:
        holder_list.append(generate_char(birth_year,family,id_num))
        end_year = holder_list[-1].death
        birth_year = holder_list[-1].birth + random_birth_offset()
        id_num = id_num+1
    #Build the actual id's of the characters and the parental history
    for holder,list_loc in zip(holder_list,range(len(holder_list))):
        holder.id_num = base_str+str(holder.id_num).zfill(3)
        if list_loc>0: holder_list[list_loc].father = holder_list[list_loc-1].id_num
    return holder_list

def generate_title_history(holder_list,government='tribal_government'):
    title_history = []
    title_holder = []
    for holder,list_loc in zip(holder_list,range(len(holder_list))):
        if list_loc == 0:
            title_holder = TitleHolder(holder.id_num,holder.birth+16,holder.death,government)
        else:
            title_holder = TitleHolder(holder.id_num,holder_list[list_loc-1].death,holder.death,government)
        title_history.append(title_holder)
    return title_history