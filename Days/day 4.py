# head and tales program

import random

digit = random.randint (1,2)

if digit == 1:
    print ("Heads")
else:
    print ("Tales")

##########################################

# list things

beta = random.seed()
print (beta)


li = [ "most", "blau", "king"]
print(li[1])
li[2] = "blu"
li.append ("meow")
print (li)
li.extend (["honk", "futu", "gimbo","vamus"])
print (li)
li.insert(0, "niachi")
print(li)
li.insert(len(li) - 1, "figgabuchi")
print (li)
li.append("karol")
print (li)
li.remove("jiono")
print (li)
print (li.count("cod"))
li.choice()
