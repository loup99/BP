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
              ('Eastern Syriac Church',[0.8,0.3,0.5])]

make_hex = lambda x : str(hex(round(255*x))).replace('0x','').zfill(2)
make_color = lambda x : make_hex(x[0])+make_hex(x[1])+make_hex(x[2])

file_text = []
with open('Faith.html','r') as f:
    file_text = f.readlines()
for line,ind in zip(file_text,range(len(file_text))):
    for faith in faith_list:
        if ">"+faith[0]+"<" in line:
            color_string = make_color(faith[1]).replace('0x','')
            file_text[ind] = '<td style="background-color:#'+color_string+'"'+line[3:]
with open('Faith.html','w') as f:
    f.writelines(file_text)
