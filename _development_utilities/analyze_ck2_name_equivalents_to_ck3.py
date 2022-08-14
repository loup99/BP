import sys

#To Use: Takes a list of CK2 name equivalents (like Adamos_Adam) and converts them
#to CK3 scheme equivalence files. Requires the sex (male, female) as a command line input

#Inputs
sex = sys.argv[1]
#Open the file
with open('ck2_'+sex+'_names.txt','r',encoding="utf-8-sig") as f:
    file_text = f.readlines()
file_text = [item.replace('\n','') for item in file_text]
file_text = [item.split('+') for item in file_text]
#Check for errors
index = 0
for item in file_text:
    index += 1
    if ( len(item)>2 ):
        print('Index '+str(index)+' is length '+str(len(item)))
#Create dictionary
the_keys = list(set([item[1] for item in file_text]))
the_keys.sort()
the_dictionary = {item: [item] for item in the_keys}
for item in file_text:
    key_value = item[1]
    old_list = the_dictionary[key_value]
    old_list.append(item[0])
    new_list = list(set(old_list))
    the_dictionary.update(key_value=new_list)
with open('ck2_equivalences_'+sex+'_names.txt','w') as f:
    for key in the_dictionary:
        if ( key != 'key_value'):
            f.write(key+'_'+sex+' = { ')
            for item in set(the_dictionary[key]):
                f.write(item+' ')
            f.write('}\r\n')