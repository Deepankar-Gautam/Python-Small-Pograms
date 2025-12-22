import random

Letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

Numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

Special_characters = [
    "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", 
    "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", 
    "]", "^", "_", "`", "{", "|", "}", "~"
]

print ("Welcome to Random Password Generator")
let = int(input("How many Letters do you want in your Password?\n"))
num = int(input("How many Numbers do you want in your Password?\n"))
spe = int(input("How many Special Characters do you want in your Password?\n"))

#######################  Easy level  #######################

password = ""

for ch in range(let):
    let_pass = random.choice(Letters)
    password += let_pass

for ch in range (num):
    num_pass = random.choice(Numbers)
    password += num_pass

for ch in range (spe):
    spe_pass = random.choice(Special_characters)
    password += spe_pass
    
print ("Your Generated password is : ", password)

#######################  Hard level  #######################

password_list = []
password = ""

for ch in range (let):
    let_pass = random.choice(Letters)
    password_list.append(let_pass)

   
for ch in range (num):
    num_pass = random.choice(Numbers)
    password_list.append(num_pass)

for ch in range (spe):
    spe_pass = random.choice(Special_characters)
    password_list.append(spe_pass)

random.shuffle(password_list)
password = "".join(password_list)

print ("Your Generated password is : ", password)
