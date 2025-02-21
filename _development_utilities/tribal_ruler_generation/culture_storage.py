from .data_types import Culture

#List of Cultures
test_roman = Culture('roman',
                    ['Maximus','Gaius','Quintus','Canis'],
                    ['dynn_Nepos','dynn_Iulius','dynn_Augustus','dynn_Robertus'],
                    father_name_chance = 0.35,
                    grandfather_name_chance = 0.35)
sami = Culture('sami',
               ["A_ggi","A_igesA_rri","A_ilu","A_mmot","A_ra","A_rrajuoksa","A_sllat","E_oavvA_","Ahkemiella",
                "Algebaeivi","Baeivi","Baeivvet","Biejan","BijA_s","Bilzi","DA_vgon","DuttA_","GA_ivvas",
                "GA_ktu","Henes","JA_rre","Jeansa","Juvven","LA_gon","LA_vrrohas","LeammA_","Mellet","Mihka","Mohkku",
                "Mokci","NA_hkol","NA_innas","Njulgu","OavA_n","Orddot","RA_stos","Riibma","Ruigi","SA_rra",
                "Speaidna","Viggu"],
               ["dynn_Ahkebeaivi","dynn_Ahkemiella","dynn_GA_ivvaS_","dynn_Varakid","dynn_Sarakid","dynn_Hasabid",\
                "dynn_Tatvid","dynn_Yurakid","dynn_Jio","dynn_Simo","dynn_Kuni","dynn_Rahna","dynn_Sochioch",\
                "dynn_Jochmoch","dynn_Avioware","dynn_Enare","dynn_Enaraby","dynn_Kimi","dynn_Suenekelle",\
                "dynn_Warager","dynn_Teno","dynn_Maggeroe","dynn_Kittilaby","dynn_Sambeaoby","dynn_Pajersvi",\
                "dynn_Kielit","dynn_Kemeloe"],
               father_name_chance = 0.0,
               grandfather_name_chance = 0.0,
              )

culture_list = {'test_roman':test_roman,
                'sami':sami}
