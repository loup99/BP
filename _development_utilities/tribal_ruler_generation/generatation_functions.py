from numpy import random as rand
from .data_types import *

random_select = lambda the_list: rand.randint(0,len(the_list))
random_birth_offset = lambda: round(rand.normal(22.0,scale=3.5))

#Wrapper for randomly generating a dynasty, given a culture
def makeDynasty(id_num,culture):
    name = culture.dynasty_name_list[random_select(culture.dynasty_name_list)]
    return Dynasty(name,id_num,culture.name)

#Wrapper for making a holder, because Python only likes a single constructor
def makeCharacter(family,birth,death,name,id_num=0,father=None):
    return Character(family.culture.name,
                  family.dynasty.id_num,
                  family.religion,
                  birth,
                  death,
                  name,
                  id_num,
                  father)

#Generates a single character
def generate_char(birth_year,family,id_num=0):
    name = family.culture.male_name_list[random_select(family.culture.male_name_list)]
    death_year = max(round(rand.normal(loc=birth_year+40,scale=16.0)),17)
    return makeCharacter(family,birth_year,death_year,name,id_num,None)

#The min values should prevent kids too early or dying at the wrong time
def generate_characters(base_str,culture,religion,start_year,stop_year,start_id_num=0):
    #Build the family
    dynasty = makeDynasty('dynn_'+base_str,culture)
    family = Family(culture,dynasty,religion)
    #Renaming odds
    father_name_interval = [0,culture.father_name_chance]
    grandfather_name_interval = [culture.father_name_chance,culture.father_name_chance+culture.grandfather_name_chance]
    #Initialize the character list
    character_list = []
    id_num = start_id_num
    #Initial loop variables
    birth_year = min(start_year - random_birth_offset(),start_year-17)
    end_year = start_year
    #Actually generate holders
    while end_year <= stop_year:
        character_list.append(generate_char(birth_year,family,id_num))
        end_year = character_list[-1].death
        birth_year = min(character_list[-1].birth + random_birth_offset(),character_list[-1].birth+17)
        id_num = id_num+1
    #Build the actual id's of the characters and the parental history
    for holder,list_loc in zip(character_list,range(len(character_list))):
        holder.id_num = base_str+str(holder.id_num).zfill(3)
        if list_loc>0: character_list[list_loc].father = character_list[list_loc-1].id_num
        #Odds of being named father/grandfather
        rename_roll = rand.uniform(0,1)
        if (father_name_interval[0]<rename_roll) and (rename_roll<father_name_interval[1]):
            if list_loc>0:
                character_list[list_loc].name = character_list[list_loc-1].name
        elif (grandfather_name_interval[0]<rename_roll) and (rename_roll<grandfather_name_interval[1]):
            if list_loc>1:
                character_list[list_loc].name = character_list[list_loc-2].name
        #Prevent sons from pre-deceasing their fathers
        if list_loc>0:
            if character_list[list_loc].death < character_list[list_loc-1].death:
                character_list[list_loc].death = character_list[list_loc-1].death+rand.randint(5,15)
    return character_list,dynasty

def generate_title_history(character_list,government='tribal_government'):
    title_history = []
    title_holder = []
    for holder,list_loc in zip(character_list,range(len(character_list))):
        if list_loc == 0:
            title_holder = TitleHolder(holder.id_num,holder.birth+16,holder.death,government)
        else:
            title_holder = TitleHolder(holder.id_num,character_list[list_loc-1].death,holder.death,government)
        title_history.append(title_holder)
    return title_history