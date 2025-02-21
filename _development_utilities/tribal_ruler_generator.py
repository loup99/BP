from tribal_ruler_generation.data_types import *
from tribal_ruler_generation.generatation_functions import *
import tribal_ruler_generation.culture_storage as culture_storage

'''
This is code for generating fictional tribal holders in places far removed from recorded civilization.
It presumes no change in culture or religion and just builds a line of rulers for various titles.
'''

#TODO: Print character list in PDX format
#TODO: Print holding history in PDX format (with and without government addition for first holder)
#TODO: Print dynasty data in PDX format

#TODO: Weight name selection by father/grandfather weights (attach to culture data struct)

##### Main #####

culture = culture_storage.culture_list['test_roman']

holders = generate_holders('exampleChars',culture,'nicene',395,500)
title_history = generate_title_history(holders)
for holder in holders:
    print(holder)
for holder in title_history:
    print(holder)
