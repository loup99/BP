def update_html_file(fname,item_list):
    with open(fname,'r') as f:
        file_text = f.readlines()
    #Count instances of item
    item_total_instances = []
    for item in item_list:
        total_instances = 0
        for line in file_text:
            if ('p>'+item+'</p') in line:
                total_instances+=1
        item_total_instances.append(total_instances)
    #Clean up item instances
    for item_ind in range(len(item_list)):
        item = item_list[item_ind]
        for line_ind in range(len(file_text)):
            if ( item_list[item_ind] in file_text[line_ind] ):
                file_text[line_ind] = '<td style="text-align: center;" rowspan='+str(item_total_instances[item_ind])+'>'+item+'</td>\r\n'
                break
    #Remove duplicates
    for item in item_list:
        new_file_text = []
        for line in file_text:
            if ( ('<p>'+item+'</p>') not in line):
                new_file_text.append(line)
        file_text = new_file_text
    #Ovewrite old file
    with open(fname,'w') as f:
        f.writelines(file_text)

#TODO: Replace hard-coding with querying table files
creeds = ['Chalcedonian Creed',\
          'Miaphysite Creed',\
          'Eastern Creed',\
          'Arian Creed']
groups = ['Western Dyophysites',\
          'Miaphysites',\
          'Eastern Dyophysites',\
          'Arians',\
          'Monophysites',\
          'Gnostics',\
          'Antinomians',\
          'Major',\
          'Minor']
shared_hof = ['Roman Patriarchate',\
              'Patriarch of Alexandria',\
              'Apostolic Church']

faith_fname = 'Faith.html'
update_html_file(faith_fname,creeds)
update_html_file(faith_fname,groups)
update_html_file(faith_fname,shared_hof)

heritages = ['Anatolian_Heritage',\
             'Byzantine_Heritage',\
             'Caucasian_Heritage',\
             'Proto-Carpathian_Heritage',\
             #Balto-Slavic
             'Baltic_Heritage',\
             'East Slavic_Heritage']

culture_fname = 'Culture.html'
update_html_file(culture_fname,heritages)
