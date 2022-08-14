import sys
import check_suffix_item as csi

if __name__ == '__main__':
    errors_found = False
    # root_dir needs a trailing slash (i.e. /root/dir/)
    root_dir = './volkerwanderung/'
    exceptions_dir = '.test_scripts/_check_database_known_errors/'
    item_type_list = ['scripted_triggers','scripted_effects']
    
    for item_type in item_type_list:
        suffix = csi.only_allow_effects_and_trigger(item_type)
        exceptions_fname = exceptions_dir+item_type+csi.exception_file_suffix+'.txt'
        test_error_found = csi.run_test(root_dir,item_type,suffix,exceptions_fname)
        if ( not test_error_found ):
            print('No '+item_type+' issues found')
        errors_found |= test_error_found
    
    if ( errors_found ):
        sys.exit(1)