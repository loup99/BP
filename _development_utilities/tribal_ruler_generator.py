from tribal_ruler_generation.data_types import *
from tribal_ruler_generation.generatation_functions import *
from tribal_ruler_generation.print_data import *
import tribal_ruler_generation.culture_storage as culture_storage

'''
This is code for generating fictional tribal holders in places far removed from recorded civilization.
It presumes no change in culture or religion and just builds a line of rulers for various titles.
'''

##### Main #####
start_year = 400
end_year = 550
religion = 'germanic_pagan'
culture = culture_storage.culture_list['dane']

## Saami Peoples
#holding_list = ["c_kakisalmi","c_sortavala","c_salinis","c_onega","c_kontupohja","c_viena","c_viipuri","c_nyland",
#                "c_finland","c_tavasts","c_messukyla","c_satakunta","c_olavinlinna","c_pielinen","c_sysma","c_oulu",
#                "c_pedersore","c_kainuu","c_mustasaari","c_sjeltie","c_ubmejeiednuo","c_pite",
#                "c_jahkamakke","c_biton","c_julevadno","c_kittila","c_torne","c_siggevara","c_suondavara","c_rounala",
#                "c_aviovara","c_karasjohka","c_peaccam","c_kitka","c_koutajoki","c_akkel","c_sombio","c_inari",
#                "c_skolt","c_ter","c_jovvkuj","c_east_kiilt","c_kintus","c_halsingland","c_medelpad","c_angermanland",
#                "c_vastvag","c_bothin","c_jamtfir","c_morarna","c_helgum","c_harjadalen","c_hedmork","c_gudbrandsdalir",
#                "c_eystridalir","c_gauldala","c_aland","c_varmland","c_dalarna","c_nordmark",
#                "c_onega_BJA","c_povenets"]

##Bjarmaland Permians & Permia Permians (komi)
#holding_list = ["c_kholmogory","c_kevrola","c_velsk","c_shenkursk","c_ustyug",
#                "c_elabuga", #Volga Bulgraia
#                "c_perm","c_sebur","c_lysva","c_kumych","c_ural","c_votkinsk","c_kerken","c_kargadan","c_palniki","c_glazov","c_kolyn"]

##Bjarmaland Fenni
#holding_list = ["c_pudozh","c_kargopol","c_kirillov","c_totma","c_vologda","c_lyubim","c_onsthia","c_choklema"]Novgord sans Pskov

##Novgord
#holding_list = ["c_novgorod","c_rusa","c_pskov","c_sebezh","c_vodi","c_beloozero","c_tikhvin","c_vyangi","c_luki","c_valdai","c_bezichi"]

##Estonia sans Latigalians
#holding_list = ["c_reval","c_narva","c_osel","c_wiek","c_vidzeme","c_livs","c_dorpat","c_aluksne"]

##Merya counties
#holding_list = ["c_tver","c_yaroslavl","c_suzdal","c_plyos","c_maturovo"]

##Muroma
#holding_list = ["c_murom"]

##Muroma
#holding_list = ["c_vladmir","c_moskva","c_tula","c_odoyev","c_novosil","c_ryazan"]

#Mari
#holding_list = ["c_nizhny_novgorod","c_yoshkar-ola","c_martyuba","c_cykma","c_kazan"]

##Mordvins
#holding_list = ["c_cheboksary","c_kozlov","c_lachyk-uba","c_saran","c_voronezh","c_karatayak","c_penza","c_petrovsk","c_tuluchezeva","c_tambov","c_durovka",
#                "c_ashli"]

##Gorkhovo
#holding_list = ["c_uraltau","c_karabash","c_uiska","c_yekaterinburg","c_chelabinsk","c_chadrinsk","c_jitikul","c_atamansku","c_kurgan","c_sabakyul"]

##Sargat
#holding_list = ["c_vargashi","c_petropavl","c_teke","c_kainsk","c_omsk","c_petropavolsk","c_tara","c_ishim","c_dolgujar","c_kazanskoye"]

##Khanty
#holding_list = ["c_sibir","c_tobol","c_belogorje","c_bardak","c_tyumen","c_laia","c_tabary","c_neramkary","c_tselym_dalyn","c_kharam-vosh","c_kartauzh","c_pelym","c_koshuki","c_kazym","c_sosva","c_koda"]

##Samoyed
#holding_list = ["c_ob","c_biia","c_torema","c_sorok","c_kondoma","c_kyin","c_vasyugan","c_umiai","c_tartas_SIB","c_chich","c_kolyvan","c_sartlan","c_ubins","c_igaran","c_konda_ob","c_kulunda","c_barnaul"]

##Yeniseian
#holding_list = ["c_tomsk","c_kiia","c_taskyl","c_kojuk","c_chulym","c_narim","c_sochur","c_yenisei","c_krasnoyarsk","c_mana","c_shishina","c_kansk","c_tagul","c_chuna","c_bratsk","c_tulun"]

##Tungusic
#holding_list = ["c_kotera","c_vitim","c_karabaigal","c_chuya","c_baigaluuls","c_uulynkhol"]

##Pannonian Subei: Post Bolia
#holding_list = ["c_sopron","c_pitten","c_vienna","c_hohenau"]

##Pannonian Huns: Post Nedao
#holding_list = ["c_baranya","c_vas","c_tolna"]
#holding_list = ["c_kolon"]

##Pannonian Romano-Pannonians (poor-souls)
#holding_list = ["c_szekesfehervar","c_veszprem","c_vukovar","c_zagorje","c_zagreb","c_pozega"]
#holding_list = ["c_somogy"]

##Romano-Illyrian Pannonians
#holding_list = ["c_vrbas",'c_soli']

##Illyrians
#holding_list = ["c_vodica","c_srebrenik"]

##Carpodaci: 450 onwards
#holding_list = ["c_barcasag","c_tabla_butii","c_galati","c_barlad","c_stoenesti","c_iasi","c_dorohoi","c_neamt","c_suceava"]

##Romano-Dacians: 450 onwards
#holding_list = ["c_campulung","c_fogaras","c_szekelyfold"]

##Vistula Veneti
#holding_list = ["d_vistula_veneti"]

##East Galindians
#holding_list = ["d_east_galindian"]

##Various Slavs:
#holding_list = ["d_kolochins"]

##Visclan/Przewosrsk
#holding_list = ["c_tarnowska","c_sacz","c_krakowska","c_cieszyn","c_ratibor","c_bethen","c_sandomierska","c_opole","c_wielunska","c_miliez","c_legnica","c_wschowska","c_schweibus","c_kaliska","c_sieradzka","c_leczycka","c_gnieznienska","c_poznanska"]

#Guti/Wielbark
#holding_list = ["c_stezycka","c_radom","c_czerska","c_gostyninksa","c_zakroczymska","c_plocka","c_dobrzyn","c_kujway","c_torun"]

##Vidivarii
#holding_list = ["d_vidivarii"]
#holding_list = ["c_slupsk","c_danzig","c_berent","c_malbork"]

##Denziner
#holding_list = ["c_stettin","c_soldin","c_kolobrzeg","c_cammin","c_landsberg","c_pila","c_miastko","c_krajna"]

##Gustow
#holding_list = ["c_rugen","c_wolgast"]

###Warnic
#holding_list = ["c_ruppin","c_prenzlau","c_brandenburg","c_werle"]
#holding_list = ["d_warini"]
#holding_list = ["c_werle"]

#Lebus
#holding_list = ["c_berlin","c_juterbog","c_wittenberg","c_brene","c_spreewald","c_grunberg","c_meissen","c_dresden","c_cottbus","c_naumberg","c_sprottau","c_gorlitz","c_przemkow"]
#holding_list = ["c_lubusz"]

##Old Saxon
#holding_list = ["d_nordalbingia"]

#Danes
holding_list = ["c_halland","c_blekinge"]

##Rump Langobard
#holding_list = ["c_brzeg","c_breslau","c_nysa"]

##North Caucasian Huns
#holding_list = ["k_north_caucasian_huns"]

##Visigothic Romano-Hispanics
#holding_list = ["d_scalabitanus"]

##Visigothic Alans
#holding_list = ["c_alcacer_do_sal"]

##Var Confederation
#holding_list = ["k_var"]

#Random Tiele holders
#holding_list = ["c_karasu","c_teniz","c_eghiz_kara","c_ulytau","c_kaska","c_astana","c_atbasar","c_shchuchinsk","c_kush-murun"]

##Barbaria of Sardinia
#holding_list = ["c_barbaria"]

##Norse of Brondings
#holding_list = ["d_brondings"]

##Slavs under Hunnic domination
#holding_list = ["c_tigheci","c_chilia","c_cetatea_alba","c_lapusna"]

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
