from tribal_ruler_generation.data_types import *
from tribal_ruler_generation.generatation_functions import *
from tribal_ruler_generation.print_data import *
import tribal_ruler_generation.culture_storage as culture_storage

'''
This is code for generating fictional tribal holders in places far removed from recorded civilization.
It presumes no change in culture or religion and just builds a line of rulers for various titles.
'''

##### Main #####
start_year = 395
end_year = 500
religion = 'finnish_pagan'
culture = culture_storage.culture_list['sami']
holding_list = ["c_kakisalmi","c_sortavala","c_salinis","c_onega","c_kontupohja","c_viena","c_viipuri","c_nyland",
                "c_finland","c_tavasts","c_messukyla","c_satakunta","c_olavinlinna","c_pielinen","c_sysma","c_oulu",
                "c_kainuu","c_pietarsaari","c_mustasaari","c_sjeltie","c_ubmejeiednuo","c_pite","c_jahkamakke",
                "c_biton","c_julevadno","c_kittila","c_torne","c_siggevara","c_suondavara","c_rounala","c_aviovara",
                "c_karasjohka","c_peaccam","c_kitka","c_koutajoki","c_akkel","c_sombio","c_inari","c_skolt","c_ter",
                "c_jovvkuj","c_east_kiilt","c_kintus","c_halsingland","c_medelpad","c_angermanland","c_vastvag",
                "c_bothin","c_namdalfylki","c_jamtfir","c_morarna","c_helgum","c_harjadalen","c_hedmork",
                "c_gudbrandsdalir","c_eystridalir","c_gauldala","c_aland","c_varmland","c_dalarna","c_nordmark"]

for holding,list_loc in zip(holding_list,range(len(holding_list))):
    #Write or append data
    write_mode = 'w' if list_loc==0 else 'a'
    #Generate the holding data
    characters,dynasty = generate_characters('holder_'+holding,culture,religion,start_year,end_year,0)
    title_history = generate_title_history(characters)
    #print the holding data
    print_character_history(characters,religion,'example_characters.txt',write_mode)
    print_dynasty(dynasty,'example_dynasty.txt',write_mode)
    print_title_history(holding,title_history,'example_title_history.txt',write_mode)
