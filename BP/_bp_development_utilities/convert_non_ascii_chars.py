# -*- coding:utf-8 -*-

#Original Code taken from
#https://stackoverflow.com/questions/50853004/python-convert-utf8-special-characters-accented-to-extended-ascii-equivalent
#And modified for our purposes

import sys

#To Use: Takes an input/output file with special characters (like CK2 �ahrux) and makes a CK3 equivalent
#(like S_ahrux).

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
        elif codepoint == 0x00c0: #�
            retval.append('A_')
            continue
        elif codepoint == 0x00c1: #�
            retval.append('A_')
            continue
        elif codepoint == 0x00c2: #�
            retval.append('A_')
            continue
        elif codepoint == 0x00c3: #�
            retval.append('A_')
            continue
        elif codepoint == 0x00c4: #�
            retval.append('A_')
            continue
        elif codepoint == 0x00c5: #�
            retval.append('A_')
            continue
        elif codepoint == 0x00c6: #�
            retval.append('AE_')
            continue
        elif codepoint == 0x00c7: #�
            retval.append('C_')
            continue
        elif codepoint == 0x00c8: #�
            retval.append('E_')
            continue
        elif codepoint == 0x00c9: #�
            retval.append('E_')
            continue
        elif codepoint == 0x00ca: #�
            retval.append('E_')
            continue
        elif codepoint == 0x00cb: #�
            retval.append('E_')
            continue
        elif codepoint == 0x00cc: #�
            retval.append('I_')
            continue
        elif codepoint == 0x00cd: #�
            retval.append('I_')
            continue
        elif codepoint == 0x00ce: #�
            retval.append('I_')
            continue
        elif codepoint == 0x00cf: #�
            retval.append('I_')
            continue
        elif codepoint == 0x00d0: #�
            retval.append('D_')
            continue
        elif codepoint == 0x00d1: #�
            retval.append('N_')
            continue
        elif codepoint == 0x00d2: #�
            retval.append('O_')
            continue
        elif codepoint == 0x00d3: #�
            retval.append('O_')
            continue
        elif codepoint == 0x00d4: #�
            retval.append('O_')
            continue
        elif codepoint == 0x00d5: #�
            retval.append('O_')
            continue
        elif codepoint == 0x00d6: #�
            retval.append('O_')
            continue
        #Skip 0x00d7
        elif codepoint == 0x00d8: #�
            retval.append('O_')
            continue
        elif codepoint == 0x00d9: #�
            retval.append('U_')
            continue
        elif codepoint == 0x00da: #�
            retval.append('U_')
            continue
        elif codepoint == 0x00db: #�
            retval.append('U_')
            continue
        elif codepoint == 0x00dc: #�
            retval.append('U_')
            continue
        elif codepoint == 0x00dd: #�
            retval.append('Y_')
            continue
        elif codepoint == 0x00de: #�
            retval.append('TH_')
            continue
        elif codepoint == 0x00df: #�
            retval.append('SS_')
            continue
        elif codepoint == 0x00e0: #�
            retval.append('a_')
            continue
        elif codepoint == 0x00e1: #�
            retval.append('a_')
            continue
        elif codepoint == 0x00e2: #�
            retval.append('a_')
            continue
        elif codepoint == 0x00e3: #�
            retval.append('a_')
            continue
        elif codepoint == 0x00e4: #�
            retval.append('a_')
            continue
        elif codepoint == 0x00e5: #�
            retval.append('a_')
            continue
        elif codepoint == 0x00e6: #�
            retval.append('ae_')
            continue
        elif codepoint == 0x00e7: #�
            retval.append('c_')
            continue
        elif codepoint == 0x00e8: #�
            retval.append('e_')
            continue
        elif codepoint == 0x00e9: #�
            retval.append('e_')
            continue
        elif codepoint == 0x00ea: #�
            retval.append('e_')
            continue
        elif codepoint == 0x00eb: #�
            retval.append('e_')
            continue
        elif codepoint == 0x00ec: #�
            retval.append('i_')
            continue
        elif codepoint == 0x00ed: #�
            retval.append('i_')
            continue
        elif codepoint == 0x00ee: #�
            retval.append('i_')
            continue
        elif codepoint == 0x00ef: #�
            retval.append('i_')
            continue
        elif codepoint == 0x00f0: #�
            retval.append('d_')
            continue
        elif codepoint == 0x00f1: #�
            retval.append('n_')
            continue
        elif codepoint == 0x00f2: #�
            retval.append('n_')
            continue
        elif codepoint == 0x00f3: #�
            retval.append('o_')
            continue
        elif codepoint == 0x00f4: #�
            retval.append('o_')
            continue
        elif codepoint == 0x00f5: #�
            retval.append('o_')
            continue
        elif codepoint == 0x00f6: #�
            retval.append('o_')
            continue
        #Skip 0x00f7
        elif codepoint == 0x00f8: #�
            retval.append('o_')
            continue
        elif codepoint == 0x00f9: #�
            retval.append('u_')
            continue
        elif codepoint == 0x00fa: #�
            retval.append('u_')
            continue
        elif codepoint == 0x00fb: #�
            retval.append('u_')
            continue
        elif codepoint == 0x00fc: #�
            retval.append('u_')
            continue
        elif codepoint == 0x00fd: #�
            retval.append('y_')
            continue
        elif codepoint == 0x00fe: #�
            retval.append('th_')
            continue
        elif codepoint == 0x00ff: #�
            retval.append('y_')
            continue
        #Other found chars
        elif codepoint == 0x0160: #�
            retval.append('S_')
            continue
        elif codepoint == 0x0161: #�
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
