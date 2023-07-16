#!/usr/bin/bash
array=("c_pest:" "c_pest_adj:" "d_achaia:" "d_achaia_adj:" "d_athens:" "d_athens_adj:" "d_campania:" "d_campania_adj:" "d_catalonia:" "d_catalonia_adj:" "d_danes:" "d_danes_adj:" "d_galatia:" "d_galatia_adj:" "d_lettigalians:" "d_lettigalians_adj:" "d_muromians:" "d_muromians_adj:" "d_oxford:" "d_oxford_adj:" "d_powys:" "d_powys_adj:" "d_samarkand:" "d_samarkand_adj:" "d_sami:" "d_sami_adj:" "d_syria:" "d_syria_adj:" "d_tangiers:" "d_tangiers_adj:" "d_toulouse:" "d_toulouse_adj:" "d_tripolitania:" "d_trondelag:" "d_trondelag_adj:" "d_zemigalians:" "d_zemigalians_adj:" "e_armenia:" "e_armenia_adj:" "e_roman_empire:" "e_roman_empire_adj:" "k_alania:" "k_alania_adj:" "k_beni_helal:" "k_beni_helal_adj:" "k_byzantium:" "k_byzantium_adj:" "k_dacia:" "k_dacia_adj:" "k_israel:" "k_israel_adj:" "k_khazaria:" "k_khazaria_adj:" "k_mauretania:" "k_mauretania_adj:" "k_taurica:" "k_taurica_adj:" "d_manichean:" "e_caspian-pontic_steppe:" "e_caspian-pontic_steppe_adj:" "k_pontic_steppe:" "k_pontic_steppe_adj:" "k_caucasus:" "k_caucasis_adj:" "b_pervomaisk:" "b_engels:" "e_turkestan:" "e_turkestan_adj:" "k_tuyuhun:" "k_tuyuhun_adj:")
for item in "${array[@]}"
do
	echo "$item"
	sed -i "/$item/d" BP_titles_l_english.yml
	#sed -i "/$item/d" $(find ./dynasties -iname "*.yml")
done
