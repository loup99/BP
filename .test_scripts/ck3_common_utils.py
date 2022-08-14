import os
import re
import glob
import sys

from math import floor

'''
search_over_mod_structure
Arguments:
  root_dir: Directory Root Dir
  file_keyword: file keyword to search for in the file name (e.g., either the item type or '.+' (everything in the database)
  file_action_object: class building the data object (a dictionary or a list, depending). Must have method action
      which takes a file name as an argument
Desc:
  Finds a list of text files based on comparison of dir_name to item_type and does file_action
  (making a list of items to search over OR a dictionary of database instance counts)
'''
def search_over_mod_structure(root_dir,file_keyword,file_action_object,data_object,console_output):
    #Why don't we add localization files? Because removal of other database items might void localization items
    #So stuff that's used in only in localization (like 'clan_government_levies_max_possible') should be an
    #exclusion instead
    file_list = [y for x in os.walk(root_dir) for y in glob.glob(os.path.join(x[0], '*.txt'))]
    for file,index in zip(file_list,range(len(file_list))):
        if ( console_output ): task_progress_meter(index,len(file_list))
        if ( re.search(file_keyword,file) ):
            if ( isinstance(data_object,list) ):
                data_object.extend(file_action_object.action(file))
            else:
                data_object = file_action_object.action(file)
    if ( console_output ): task_progress_meter(len(file_list),len(file_list))
    return data_object

def task_progress_meter(workDone,totalWork):
    progress_meter_len = 20
    fracWorkDone = floor((workDone/totalWork)*progress_meter_len)
    progress_meter_string = '['+'-'*fracWorkDone+' '*(progress_meter_len-fracWorkDone)+']'
    print('\r'+progress_meter_string,end='')

def load_exceptions_list(fname):
    exception_list = []
    with open(fname,'r',encoding='utf-8') as f:
        for line in f:
            if ( not '#' in line ):
                exception_list.append(line.replace('\n',''))
    return list(set(exception_list))

def remove_exceptions_list(item_list,exception_list):
    return list(set(item_list)-set(exception_list))

def console_input_parsing(exception_file_suffix):
    root_dir = './'+sys.argv[1]
    exceptions_dir = '.test_scripts/_check_database_known_errors/'
    item_type = sys.argv[2]
    #Exceptions file handling
    exceptions_fname = ''
    if(len(sys.argv)>3):
        exceptions_fname = sys.argv[3]
    else:
        exceptions_fname = exceptions_dir+item_type+exception_file_suffix+'.txt'
    return root_dir,item_type,exceptions_fname

def common_exit(errors_found,item_type):
    if ( errors_found ):
        sys.exit(1)
    else:
        print('No '+item_type+' issues found')
        sys.exit(0)