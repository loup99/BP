import sys
import os
import re
from collections import Counter

from ck3_common_utils import search_over_mod_structure
from ck3_common_utils import load_exceptions_list
from ck3_common_utils import remove_exceptions_list
from ck3_common_utils import console_input_parsing
from ck3_common_utils import common_exit

'''
Searches your CK3 mod with regex for common/ database items. For Python 3.

Requires dotnet-script SDK 6.0+ to be installed; see https://dotnet.microsoft.com/en-us/download/dotnet/6.0 for
installation instructions

This will throw a failure when:
    A database entry is unused (and thus is superfluous)
    A database entry has a duplicate (and thus the game will resolve this for you, possibly in a way you don't want)

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

Arg 2 is the item type (scripted_triggers, &c.)
    Currently tested on script_values, scripted_triggers, scripted_effects

Arg 3 is the locations of your exceptions file (e.g., things you overwrite from Vanilla that might not
have references in your codebase). By default, it looks at:
./MOD/.test_scripts/_check_database_known_errors/<item_type>_database_exceptions.txt

Example run command: "python3 .test_scripts/check_database_item.py MY_MOD_NAME scripted_triggers"

Note 1: -1 failures returns indicate some of your items are contained in others in terms of regular expressions.
Consider rewriting such items to avoid those failures if you want to use this code. If you don't want to rename
your database entries, add them to your exceptions file.

Aside: It is not recommended to do this as PDX updates may cause things to break and your exceptions in a way
that could hide things; additionally, as PDX mod files are txt, they are highly amenable to regex searches

Example of -1 instance failure case: bog_standard_trigger and bog_standard_trigger_version2 will mean 
bog_standard_trigger_version2 will have -1 instances

Note 2: This is a quick piece of code and isn't optimized. There's probably some O(horrifying) naive
implementations here, but it runs fast enough (<30 seconds) to analyze script_values, scripted_effects, and
scripted_triggers on a total conversion mod. Should be suitable runtime for merge commit checks on main, at least.
Remember:  “Premature optimization is the root of all evil” - Donald Knuth
'''

''' License: BSD Zero Clause
Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN
AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE
OF THIS SOFTWARE.
'''

exception_file_suffix = '_database_exceptions'

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
        stream = os.popen(f'dotnet-script .test_scripts/get_items_in_file.csx {file}')
        output = stream.read()
        item_list = output.strip().split(' ')
        return item_list

#Wrapper Class for counting instances of item_types we want to check
class CountInstancesOfItemsInFileList:
    #Build our monsterous regex pattern
    def __init__(self,item_list):
        regex_pattern = ''
        for item in item_list:
            regex_pattern += item
            regex_pattern += '|'
        regex_pattern = regex_pattern[:-1] #Because we keep padding |, remove the last char
        self.regex_pattern = '('+regex_pattern+')'
        self.item_dict = { i : 0 for i in item_list }
    '''
    Arguments:
      root_dir: Directory Root Dir
      dir_name: Directory we're search
    Desc
      Counts instances of each item in a file
    '''
    def action(self,file):
        with open(file,'r',encoding='utf-8') as file_obj:
            for line in file_obj:
                if ( line[0] != '#' ):
                    for match in re.finditer(self.regex_pattern,line):
                        self.item_dict.update({match[0]:self.item_dict[match[0]]+1})
        return self.item_dict

#Because we should always have a value of 1 (i.g., defined in the item_type database), decrement the instances by 1
def decrement_dictionary_values(input_dict):
    for key, value in input_dict.items():
        input_dict.update({key:value-1})
    return input_dict

def determine_database_failure(input_dict):
    failure_list = []
    for key,value in input_dict.items():
        if ( input_dict[key] <= 0 ):
            failure_list.append( (key,value) )
    return failure_list

def run_test(root_dir,item_type,exceptions_fname,console_output=False):
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
    if(console_output): print('\n')
    #Do a quick check for duplicates (some other undesirable behavior)
    if(console_output): print('Checking Duplicates')
    duplicates = [k for k, v in Counter(item_list).items() if v > 1]
    item_list = remove_exceptions_list(item_list,exception_list)
    if(console_output): print('\n')
    #Now we'll search everything **but** item_type folder for triggers
    #Note that we want to search the item folder because some items are used within other items in the item folders
    #(think nested triggers)
    if(console_output): print('Counting '+item_type+' Usage')
    database_count = CountInstancesOfItemsInFileList(item_list)
    item_usage = search_over_mod_structure(root_dir,'.+',database_count,{},console_output)
    item_usage = decrement_dictionary_values(item_usage)
    failed_items = determine_database_failure(item_usage)
    if(console_output): print('\n')
    #Summary:
    if ( len(duplicates)>0 ):
        errors_found = True
        print('Duplicate '+item_type+':\n'+str(duplicates))
    if ( len(failed_items)>0 ):
        errors_found = True
        print('Failed '+item_type+':\n'+str(failed_items))
    return errors_found

if __name__ == '__main__':
    root_dir,item_type,exceptions_fname = console_input_parsing(exception_file_suffix)
    
    errors_found = run_test(root_dir,item_type,exceptions_fname,True)
    
    common_exit(errors_found,item_type)
