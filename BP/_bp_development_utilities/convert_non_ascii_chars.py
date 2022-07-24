# -*- coding:utf-8 -*-

#Original Code taken from
#https://stackoverflow.com/questions/50853004/python-convert-utf8-special-characters-accented-to-extended-ascii-equivalent
#And modified for our purposes

import sys

#Converts an invalid UTF-8 char to a CK3 ASCII format
def get_appropriate_char(raw):
    retval = []
    for char in raw:
        codepoint = ord(char)
        if codepoint == 0x5f: #_
            retval.append('+') #Change _ to + for word separator (for parsing purposes)
            continue
        elif codepoint < 0x80:    # Basic ASCII.
            retval.append(str(char))
            continue
        elif codepoint > 0xeffff:
            continue    # Characters in Private Use Area and above are ignored.
        elif codepoint >= 0x0080 and codepoint <= 0x009f:
            continue    # Ignore control characters in Latin-1.
        # Don't use unichr in Python 3, chr uses unicode.
        # Get character codes from here:
        # https://en.wikipedia.org/wiki/List_of_Unicode_characters#Latin-1_Supplement
        # This was written on Windows 7 32 bit
        # For 160 to 185, use what's there
        elif codepoint >= 0x00a0 and codepoint <= 0xb9:
            retval.append(str(char))
            continue
        elif codepoint == 0x00c0: #À
            retval.append('A_')
            continue
        elif codepoint == 0x00c1: #Á
            retval.append('A_')
            continue
        elif codepoint == 0x00c2: #Â
            retval.append('A_')
            continue
        elif codepoint == 0x00c3: #Ã
            retval.append('A_')
            continue
        elif codepoint == 0x00c4: #Ä
            retval.append('A_')
            continue
        elif codepoint == 0x00c5: #Å
            retval.append('A_')
            continue
        elif codepoint == 0x00c6: #Æ
            retval.append('AE_')
            continue
        elif codepoint == 0x00c7: #Ç
            retval.append('C_')
            continue
        elif codepoint == 0x00c8: #È
            retval.append('E_')
            continue
        elif codepoint == 0x00c9: #É
            retval.append('E_')
            continue
        elif codepoint == 0x00ca: #Ê
            retval.append('E_')
            continue
        elif codepoint == 0x00cb: #Ë
            retval.append('E_')
            continue
        elif codepoint == 0x00cc: #Ì
            retval.append('I_')
            continue
        elif codepoint == 0x00cd: #Í
            retval.append('I_')
            continue
        elif codepoint == 0x00ce: #Î
            retval.append('I_')
            continue
        elif codepoint == 0x00cf: #Ï
            retval.append('I_')
            continue
        elif codepoint == 0x00d0: #Ð
            retval.append('D_')
            continue
        elif codepoint == 0x00d1: #Ñ
            retval.append('N_')
            continue
        elif codepoint == 0x00d2: #Ò
            retval.append('O_')
            continue
        elif codepoint == 0x00d3: #Ó
            retval.append('O_')
            continue
        elif codepoint == 0x00d4: #Ô
            retval.append('O_')
            continue
        elif codepoint == 0x00d5: #Õ
            retval.append('O_')
            continue
        elif codepoint == 0x00d6: #Ö
            retval.append('O_')
            continue
        #Skip 0x00d7
        elif codepoint == 0x00d8: #Ø
            retval.append('O_')
            continue
        elif codepoint == 0x00d9: #Ù
            retval.append('U_')
            continue
        elif codepoint == 0x00da: #Ú
            retval.append('U_')
            continue
        elif codepoint == 0x00db: #Û
            retval.append('U_')
            continue
        elif codepoint == 0x00dc: #Ü
            retval.append('U_')
            continue
        elif codepoint == 0x00dd: #Ý
            retval.append('Y_')
            continue
        elif codepoint == 0x00de: #Þ
            retval.append('TH_')
            continue
        elif codepoint == 0x00df: #ß
            retval.append('SS_')
            continue
        elif codepoint == 0x00e0: #à
            retval.append('a_')
            continue
        elif codepoint == 0x00e1: #á
            retval.append('a_')
            continue
        elif codepoint == 0x00e2: #â
            retval.append('a_')
            continue
        elif codepoint == 0x00e3: #ã
            retval.append('a_')
            continue
        elif codepoint == 0x00e4: #ä
            retval.append('a_')
            continue
        elif codepoint == 0x00e5: #å
            retval.append('a_')
            continue
        elif codepoint == 0x00e6: #æ
            retval.append('ae_')
            continue
        elif codepoint == 0x00e7: #ç
            retval.append('c_')
            continue
        elif codepoint == 0x00e8: #è
            retval.append('e_')
            continue
        elif codepoint == 0x00e9: #é
            retval.append('e_')
            continue
        elif codepoint == 0x00ea: #ê
            retval.append('e_')
            continue
        elif codepoint == 0x00eb: #ë
            retval.append('e_')
            continue
        elif codepoint == 0x00ec: #ì
            retval.append('i_')
            continue
        elif codepoint == 0x00ed: #í
            retval.append('i_')
            continue
        elif codepoint == 0x00ee: #î
            retval.append('i_')
            continue
        elif codepoint == 0x00ef: #ï
            retval.append('i_')
            continue
        elif codepoint == 0x00f0: #ð
            retval.append('d_')
            continue
        elif codepoint == 0x00f1: #ñ
            retval.append('n_')
            continue
        elif codepoint == 0x00f2: #ò
            retval.append('n_')
            continue
        elif codepoint == 0x00f3: #ó
            retval.append('o_')
            continue
        elif codepoint == 0x00f4: #ô
            retval.append('o_')
            continue
        elif codepoint == 0x00f5: #õ
            retval.append('o_')
            continue
        elif codepoint == 0x00f6: #ö
            retval.append('o_')
            continue
        #Skip 0x00f7
        elif codepoint == 0x00f8: #ø
            retval.append('o_')
            continue
        elif codepoint == 0x00f9: #ù
            retval.append('u_')
            continue
        elif codepoint == 0x00fa: #ú
            retval.append('u_')
            continue
        elif codepoint == 0x00fb: #û
            retval.append('u_')
            continue
        elif codepoint == 0x00fc: #ü
            retval.append('u_')
            continue
        elif codepoint == 0x00fd: #ý
            retval.append('y_')
            continue
        elif codepoint == 0x00fe: #þ
            retval.append('th_')
            continue
        elif codepoint == 0x00ff: #ÿ
            retval.append('y_')
            continue
        #Other found chars
        elif codepoint == 0x0160: #Š
            retval.append('S_')
            continue
        elif codepoint == 0x0161: #š
            retval.append('s_')
            continue
        elif codepoint == 0x2019: #'
            retval.append("'")
            continue
        else:
            print('Found unhandled char!')
            print(char)
            print(hex(codepoint))
            sys.exit()
    return retval

input_file = sys.argv[1]

old_file_text = []
new_file_text = []
with open(input_file,'r',encoding="utf-8-sig") as f:
    old_file_text = f.readlines()
for line in old_file_text:
    new_line = get_appropriate_char(line)
    new_file_text.append(''.join(new_line))
with open(input_file,'w',encoding="utf-8-sig") as f:
    f.writelines(new_file_text)
