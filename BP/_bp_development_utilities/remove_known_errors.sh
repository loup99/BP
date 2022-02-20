#!/usr/bin/bash

#Combine the suppression error patterns
cat _BP_known_vanilla_errors.info _BP_known_mod_errors.info > _bp_tmp_pattern_file.info
#Greps the known errors, does the inverst match and replaces the error.log
grep -Fvf _bp_tmp_pattern_file.info error.log > tmp_error.log
#This will fail if file is locked (aka game is running)
mv tmp_error.log error.log