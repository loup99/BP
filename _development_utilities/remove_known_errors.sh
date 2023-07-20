#!/usr/bin/bash

#Greps the known errors, does the inverted match and replaces the error.log
grep -Fvf _BP_known_errors.info error.log > tmp_error1.log
mv tmp_error1.log error.log
rm tmp_error*.log