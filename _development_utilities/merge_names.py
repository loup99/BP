#!/usr/bin/python
import re

#To use: put all name equivalencies in the BP_TEST.txt files and this code will merge them all
#into a single 00_names.txt file.
name_data = []
file_text = []
with open('BP_TEST.txt','r') as f:
    file_text = f.readlines()
for line in file_text:
    data = re.split('=|{|}| ',line)
    header = data[0]
    data = data[1:]
    if ( '_female' in header ):
        sex = 'female'
    else:
        sex = 'male'
    
    header = re.split('_',header)
    header = header[:-1]
    new_header = ''
    for item in header:
        new_header += item
    new_header = new_header.lower()
    
    data = [item.replace('#','') for item in data]
    data = [item.replace('\n','') for item in data]
    data = [item for item in data if len(item)!=0]
    name_data.append([new_header,sex,set(data)])

merged_data = []
for item1 in name_data:
    header1 = item1[0]
    sex1 = item1[1]
    name_list1 = item1[2]
    for item2 in name_data:
        sex2 = item2[1]
        name_list2 = item2[2]
        if ( (sex1==sex2) and (not name_list1.isdisjoint(name_list2)) ):
            name_list1.update(name_list2)
    #Iterate over the merged data set
    already_in_set = False
    for index in range(len(merged_data)):
        sexM = merged_data[index][1]
        name_listM = merged_data[index][2]
        if ( (sexM==sex1) and (not name_list1.isdisjoint(name_listM)) ):
            already_in_set = True
            merged_data[index][2].update(name_list1)
    if ( already_in_set == False ):
        merged_data.append([header1,sex1,set(sorted(name_list1))])
#Finally sort the whole merged_data list
for index in range(len(merged_data)):
    merged_data[index][2] = sorted(merged_data[index][2])

with open('00_names.txt','w') as f:
    for item in merged_data:
        output_line = item[0]+'_'+item[1]+' = { '
        for name in item[2]:
            output_line += name+' '
        output_line += '}\n'
        f.write(output_line)
