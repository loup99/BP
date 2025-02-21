from .data_types import Culture

#List of Cultures
test_roman = Culture('roman',
                    ['Maximus','Gaius','Quintus','Canis'],
                    ['dynn_Nepos','dynn_Iulius','dynn_Augustus','dynn_Robertus'],
                    father_name_chance = 0.35,
                    grandfather_name_chance = 0.35)

culture_list = {'test_roman':test_roman}
