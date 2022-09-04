faith_list = [('Chalcedonianism','A6A65E')]


file_text = []
with open('Faith.html','r') as f:
    file_text = f.readlines()
for line,ind in zip(file_text,range(len(file_text))):
    for faith in faith_list:
        if ">"+faith[0]+"<" in line:
            file_text[ind-1] = '<td style="background-color:#'+faith[1]+'"><p><a\r\n'
with open('Faith.html','w') as f:
    f.writelines(file_text)
