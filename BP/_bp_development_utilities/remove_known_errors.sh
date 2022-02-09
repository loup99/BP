#!/usr/bin/bash

#Greps the known errors, does the inverst match and replaces the error.log
grep -Fvf _BP_known_errors.info error.log > tmp_error.log
mv tmp_error.log error.log