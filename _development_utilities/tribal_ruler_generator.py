from tribal_ruler_generation.data_types import *
from tribal_ruler_generation.generatation_functions import *
from tribal_ruler_generation.print_data import *
import tribal_ruler_generation.culture_storage as culture_storage

'''
This is code for generating fictional tribal holders in places far removed from recorded civilization.
It presumes no change in culture or religion and just builds a line of rulers for various titles.
'''

#TODO: Weight name selection by father/grandfather weights (attach to culture data struct)

##### Main #####

religion = 'nicene'
culture = culture_storage.culture_list['test_roman']

characters,dynasty = generate_holders('exampleChars',culture,religion,395,500)
title_history = generate_title_history(characters)
print_character_history(characters,religion,'example_characters.txt')
print_dynasty(dynasty,'example_dynasty.txt')
print_title_history('d_example',title_history,'example_title_history.txt')
