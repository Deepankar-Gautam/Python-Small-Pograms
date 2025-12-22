# russian roulet of "who is going to pay"

import random

names= input("Tell the names of the participents : ")
name_list = names.split(", ")
print ("\nThese are the participents", name_list)
rnd_index = random.randint(0, len(name_list) - 1)
print (f"\n{name_list[rnd_index]} is the one who is going to pay the bill of the maggie!")