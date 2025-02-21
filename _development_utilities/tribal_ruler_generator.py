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
start_year = 395
end_year = 500
religion = 'nicene'
culture = culture_storage.culture_list['test_roman']
holding_list = ['c_example_1','c_example_2']

for holding,list_loc in zip(holding_list,range(len(holding_list))):
    #Write or append data
    write_mode = 'w' if list_loc==0 else 'a'
    #Generate the holding data
    characters,dynasty = generate_holders('exampleChars',culture,religion,start_year,end_year)
    title_history = generate_title_history(characters)
    #print the holding data
    print_character_history(characters,religion,'example_characters.txt',write_mode)
    print_dynasty(dynasty,'example_dynasty.txt',write_mode)
    print_title_history(holding,title_history,'example_title_history.txt',write_mode)
