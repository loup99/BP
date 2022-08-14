import sys
import glob
import re
import os

from ck3_common_utils import search_over_mod_structure
from ck3_common_utils import load_exceptions_list
from ck3_common_utils import remove_exceptions_list
from ck3_common_utils import task_progress_meter
from ck3_common_utils import console_input_parsing
from ck3_common_utils import common_exit

'''
Ensures your scripted effects or scripted triggers are suffixed appropriately

Requires dotnet-script SDK 6.0+ to be installed; see https://dotnet.microsoft.com/en-us/download/dotnet/6.0 for
installation instructions

This will throw a failure when:
    A scripted trigger does not end with _trigger
    A scripted effect does not end with _effect

Meant to be launched from your top level git folder with structure

i.e., ./MOD/, where

./MOD/
    |- MOD/
        |- common/
        |- events/
        |- gfx/
        |- gui/
        |- localization
        |- music/

is the expected sort of underlying structure. Will need some tweaks to run under other directory structures.

Arg 1 is mod folder name

Arg 2 is the item_type (either scripted_effects or scripted_triggers)

Arg 3 is the locations of your exceptions file (e.g., things you overwrite from Vanilla that might not
have references in your codebase). By default, it looks at:
./MOD/.test_scripts/_check_database_known_errors/<item_type>_suffix_exceptions.txt

Example run command: "python3 .test_scripts/check_database_item.py MY_MOD_NAME scripted_effects"
'''

''' License: BSD Zero Clause
Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN
AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE
OF THIS SOFTWARE.
'''

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

exception_file_suffix = '_suffix_exceptions'

#Wrapper Class for building a list of items for which to search the database
class BuildItemDatabaseFromFolder:
    '''
    Arguments:
      root_dir: Directory Root Dir
      dir_name: Directory we're search
    Desc
      Pulls the list of items from the database folder
    '''
    def action(self,file):
        item_list = []
        with open(file,'r',encoding='utf-8') as file_obj:
            for line in file_obj:
                match = re.match('([A-z_]*)[\s\t]*=[\s\t]*{',line)
                if match:
                    item_list.append(match[1])
        return item_list

def check_suffixes(item_list,suffix,console_output):
    #Iterate over each item in item_list and check the appropriate suffix
    error_list = []
    for item,index in zip(item_list,range(len(item_list))):
        if ( console_output ): task_progress_meter(index,len(item_list))
        if ( not item.endswith(suffix) ):
            errors_found = True
            error_list.append(item)
    if ( console_output ): task_progress_meter(len(item_list),len(item_list))
    return error_list

def only_allow_effects_and_trigger(item_type):
    suffix = ''
    if (item_type == 'scripted_effects'):
        suffix = '_effect'
    elif ( item_type == 'scripted_triggers' ):
        suffix = '_trigger'
    else:
        print('Unable to parse argument '+item_type+'; test will not run')
        sys.exit(1)
    return suffix

def run_test(root_dir,item_type,suffix,exceptions_fname,console_output=False):
    errors_found = False
    #Load the list of exceptions if we have it
    exception_list = []
    if ( os.path.isfile(exceptions_fname) ):
        exception_list = load_exceptions_list(exceptions_fname)
    else:
        print('Note: exceptions file not found')
    #Get the list of all items in the database requested
    if(console_output): print('Building Database')
    database_build = BuildItemDatabaseFromFolder()
    item_list = search_over_mod_structure(root_dir,item_type,database_build,[],console_output)
    item_list = list(set(item_list))
    if(console_output): print('\n')
    #Remove any exceptions
    item_list = remove_exceptions_list(item_list,exception_list)
    #Check all the suffixes
    if(console_output): print('Checking Suffixes')
    error_list = check_suffixes(item_list,suffix,console_output)
    if(console_output): print('\n')
    #Summary:
    if ( len(error_list)>0 ):
        errors_found = True
        print('Improperly Formatted '+item_type+':\n'+str(error_list))
    return errors_found

if __name__ == '__main__':
    root_dir,item_type,exceptions_fname = console_input_parsing(exception_file_suffix)
    
    suffix = only_allow_effects_and_trigger(item_type)
    
    errors_found = run_test(root_dir,item_type,suffix,exceptions_fname,True)
    
    common_exit(errors_found,item_type)
