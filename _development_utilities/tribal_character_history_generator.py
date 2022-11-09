#Simpler than Jamies History Character Generator; focuses only on tribal chars and unbroken male lines
#not for use with historic characters. As such, only generates a single sex and a single line with not
#siblings

#Also will generate a templated title history file

#Uses normal distributions for both birth and death

from typing import NamedTuple
import math
from random import gauss
from random import randint

EOLChar = '\n' #Whether we want Windows or Unix EOL char, set it here

class InputValues(NamedTuple):
    character_id_string: str
    character_id_start_num: int
    
    dynasty: str
    faith: str
    culture: str
    
    starting_character_birth_year: int
    end_year: int
    #Floats so we can do math
    min_age_for_child: float
    max_age_for_child: float
    std_dev_for_child: float
    mean_for_child: float
    #Floats so we can do math
    min_death_age: float
    max_death_age: float
    std_dev_for_death: float
    mean_for_death: float

class CharacterStruct(NamedTuple):
    char_id: str
    name: str
    dynasty: str
    religion: str
    culture: str
    father: str
    birth_year: int
    death_year: int

def basic_inputs():
    return InputValues(\
        #Char id string and post-fix number
        'EstonianSetomaa',\
        0,\
        #Character data
        'estonian_dynn_setomaa',\
        'finnish_pagan',\
        'estonian',\
        #Starting year and end year
        400+randint(0,55),\
        700,\
        #Child-bearing ages; be careful to avoid overlap with death ages
        16.,\
        50.,\
        8.,\
        30.,\
        #Death ages
        40.,\
        75.,\
        10.,\
        55.)

#Converts float to int, respecting given boundaries
def set_number(num_float,minimum,maximum):
    num_float = max(num_float,minimum)
    num_float = min(num_float,maximum)
    return int(num_float)

def create_character_file(family_pole,character_file='char_data.txt'):
    with open(character_file,'w') as f:
        for char in family_pole:
            f.write( char.char_id+' = {'+EOLChar )
            f.write( '\tname = '+char.name+EOLChar )
            f.write( '\tdynasty = '+char.dynasty+EOLChar )
            f.write( '\treligion = '+char.religion+EOLChar )
            f.write( '\tculture = '+char.culture+EOLChar )
            if len(char.father)!=0:
                f.write( '\tfather = '+char.father+EOLChar )
            f.write( '\t'+str(char.birth_year)+'.1.1 = { birth = yes }'+EOLChar )
            f.write( '\t'+str(char.death_year)+'.1.1 = { death = yes }'+EOLChar )
            f.write('}'+EOLChar)

def create_title_file(family_pole,title_name='example_title',title_file='title_data.txt'):
    with open(title_file,'w') as f:
        f.write( title_name+' = {'+EOLChar )
        for ind in range(len(family_pole)):
            succession_year = 0
            char_id = family_pole[ind].char_id
            if ind==0:
                succession_year = str(family_pole[ind].birth_year+20)
            else:
                succession_year = str(family_pole[ind-1].death_year)
            f.write( '\t'+str(succession_year)+'.1.1 = { holder = '+char_id+' }'+EOLChar )
        f.write('}'+EOLChar)

if __name__ == '__main__':
    basic_values = basic_inputs()
    
    #Really not a tree, because it's just a main male line
    family_pole = []
    birth_year = basic_values.starting_character_birth_year
    generation = 0
    while birth_year < basic_values.end_year:
        #Get the age of death
        death_age = gauss(mu=basic_values.mean_for_death,sigma=basic_values.std_dev_for_death)
        death_age = set_number(death_age,basic_values.min_death_age,basic_values.max_death_age)
        #Get the age he had a kid
        had_kid_age = gauss(mu=basic_values.mean_for_child,sigma=basic_values.std_dev_for_child)
        had_kid_age = set_number(had_kid_age,basic_values.min_age_for_child,basic_values.max_age_for_child)
        #Avoid having kids after death
        if death_age < had_kid_age:
            had_kid_age = death_age
        #Get the father if not the patriarch
        if generation > 0:
            father = family_pole[generation-1].char_id
        else:
            father = []
        #Create the character
        character_data = CharacterStruct(\
            basic_values.character_id_string+str(str(generation).zfill(3)),\
            'test_name',\
            basic_values.dynasty,\
            basic_values.faith,\
            basic_values.culture,\
            father,\
            birth_year,\
            birth_year+death_age)
        family_pole.append(character_data)
        #Increment values
        birth_year += had_kid_age
        generation += 1
    #Output the associated data
    create_character_file(family_pole)
    create_title_file(family_pole)
