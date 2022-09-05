def apply_color(fname,color_list):
    make_hex = lambda x : str(hex(round(255*x))).replace('0x','').zfill(2)
    make_color = lambda x : make_hex(x[0])+make_hex(x[1])+make_hex(x[2])
    file_text = []
    with open(fname,'r') as f:
        file_text = f.readlines()
    for line,ind in zip(file_text,range(len(file_text))):
        for color in color_list:
            if ">"+color[0]+"<" in line:
                color_string = make_color(color[1]).replace('0x','')
                file_text[ind] = '<td style="background-color:#'+color_string+'"'+line[3:]
    with open(fname,'w') as f:
        f.writelines(file_text)

faith_list = [('Chalcedonianism',[0.65,0.65,0.37]),\
              ('Celtic Church',[0.23,1.0,0.23]),\
              ('Hispanic Church',[0.49,1.0,0.56]),\
              ('African Church',[1.00,0.25,0.25]),\
              ('Gallican Church',[0.10,0.10,0.60]),\
              ('Aqueleianism',[0.7,0.7,1.0]),\
              ('Iconoclasm',[0.5,0.2,0.4]),\
              ('Montanism',[0.5,0.0,0.1]),\
              ('Donatism',[0.5,0.1,0.8]),\
              ('Pelagianism',[0.5,0.9,0.55]),\
              ('Miaphysitism',[0.20,0.35,0.50]),\
              ('Western Syrian Church',[0.5,0.25,1.00]),\
              ('Ethiopian Orthodox Church',[0.40,0.35,0.50]),\
              ('Armenian Church',[0.8,0.4,0.1]),\
              ('Aghwank Church',[0.8,0.6,0.5]),\
              ('Georgian Church',[0.0,0.45,0.9]),\
              ('Eastern Syriac Church',[0.8,0.3,0.5]),\
              ('Arianism',[0.2,0.1,0.1]),\
              ('Gothic Church',[0.2,0.1,0.0]),\
              ('Pneumatomachi',[0.1,0.1,0.1]),\
              ('Monophysitism',[0.45,0.45,0.65]),\
              ('Apollinarism',[0.3,0.3,0.75]),\
              ('Eutychianism',[0.97,0.73,0.14]),\
              ('Monarchianism',[0.7,0.7,0.7]),\
              ('Marcionism',[0.7,0.1,0.4]),\
              ('Melchisdechianism',[1.0,0.5,0.7]),\
              ('Paulicianism',[0.6,0.1,0.4])]
apply_color('Faith.html',faith_list)

culture_list = [\
                #Balko-Anatolian
                ##Anatolian
                ('Cappadocian',[0.43,0.1,0.15]),\
                ('Isaurian',[0.35,0.25,0.5]),\
                ('Phrygian',[0.35,0.55,0.85]),\
                ##Byzantine
                ('Greek',[0.8,0.3,0.8]),\
                ('Pontic',[0.35,0.2,0.6]),\
                ('Helleno-Libyan',[0.70,0.20,0.90]),\
                ('Bosporan',[0.1,0.0,0.5]),\
                ('Helleno-Thracian',[0.2,0.4,0.6]),\
                ('Helleno-Aramean',[0.8,0.7,0.25]),\
                ('Helleno-Coptic',[0.70,0.30,0.70]),\
                ('Spartan_Culture',[1.0,0.4,0.4]),\
                ('Tsakonian',[0.40,0.0,0.0]),\
                ('Aeolian',[0.8,0.2,0.2]),\
                ('Massalian',[0.1,0.8,0.4]),\
                ##Caucasian
                ('Armenian',[0.5,0.2,0.5]),\
                ('Colchiscan',[0.6,0.3,0.8]),\
                ('Georgian',[0.0,0.3,0.9]),\
                ('Lazic',[0.6,0.3,0.8]),\
                ('Aghwank',[0.7,0.5,0.5]),\
                ('Nakh',[0.7,0.5,0.5]),\
                ('Abaza',[0.75,0.55,0.75]),\
                ('Adyghes',[0.6,0.3,0.8]),\
                ('Corduenian',[0.0,0.08,0.4]),\
                ##Proto-Carpathian
                ('Thracian',[0.5,0.810,0.85]),\
                ('Illyrian',[0.45,0.35,0.65]),\
                ('Dacian',[0.35,0.26,0.17]),\
                ('Macedonian',[0.7,0.5,0.5]),\
                \
                #Balto-Slavic
                ##Baltic
                ('Prussian',[0.56,0.55,0.4]),\
                ('Galindian',[0.56,0.55,0.2]),\
                ('Aesti',[0.66,0.55,0.2]),\
                ('Przeworsk',[0.6,0.4,0.2]),\
                ('Vistula Veneti',[0.6,0.6,0.1]),\
                ##East Slavic
                ('Old Slavic',[0.35,0.5,0.30])\
                ]
apply_color('Culture.html',culture_list)