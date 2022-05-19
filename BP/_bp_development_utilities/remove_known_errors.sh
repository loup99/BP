#!/usr/bin/bash

#Greps the known errors, does the inverted match and replaces the error.log
#Errors caused by PDX itself; review after every PDX patch
grep -Fvf _BP_known_vanilla_errors.info error.log > tmp_error1.log
#Errors cropping up until Main Menu by things like homeless variables (e.g., no more achievements)
grep -Fvf _BP_known_load_errors.info tmp_error1.log > tmp_error2.log
#Errors cropping up when starting a new game (i.e., not in _BP_known_load_errors)
grep -Fvf _BP_known_new_game_errors.info tmp_error2.log > tmp_error3.log
#Errors that are known and should be fixed before release, but ignored for various reasons
grep -Fvf _BP_pre_release_errors.info tmp_error3.log > tmp_error4.log
mv tmp_error4.log error.log
rm tmp_error*.log