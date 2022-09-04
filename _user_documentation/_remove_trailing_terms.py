def remove_trailing_terms(fname,term):
    remove_item = lambda line,term: line.replace(term,'')
    
    file_text = []
    with open(fname,'r') as f:
        file_text = f.readlines()
    for line_ind in range(len(file_text)):
        if term in file_text[line_ind]:
            file_text[line_ind] = remove_item(file_text[line_ind],term)
    with open(fname,'w') as f:
        f.writelines(file_text)

remove_trailing_terms('Culture.html','_Language')
remove_trailing_terms('Culture.html','_Heritage')
remove_trailing_terms('Culture.html','_Culture')