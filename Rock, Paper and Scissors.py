# Rock, Paper and Scissors

import random
print("Let's play Rock, Paper and Scissors")

user = input("So what do you choose? (Rock/Paper/Scissors)\n").lower()
possible_outputs = ["Rock", "Paper", "Scissors"]

if user not in ["rock", "paper", "scissors"]:
    print("Invalid choice! Please choose Rock, Paper, or Scissors.")

pc = random.randint(0,len(possible_outputs) -1)

rocky = ("""    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

papery = ("""     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

""")

scissory = ("""    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

""")

if user.lower() == "rock":
    print(rocky)
    print("You chose Rock")
    if pc == 0:
        print(rocky)      
        print("I chose Rock")
        print(f"Damn, you chose {user.capitalize()}, it's a draw")
    elif pc == 1:
        print(papery)      
        print("I chose Paper")  
        print(f"Yes I won because you chose {user.capitalize()}")
    else:
        print(scissory)      
        print("I chose Scissors")
        print(f"Damn bro I lost because you chose {user.capitalize()}")

elif user.lower() == "paper":
        print(papery)      
        print("You chose Paper") 
        if pc == 0:
            print(rocky)      
            print("I chose Rock")
            print(f"Damn bro I lost because you chose {user.capitalize()}")
        elif pc == 1:
            print(papery)      
            print("I chose Paper")  
            print(f"Damn, you chose {user.capitalize()}, it's a draw")
        else:
            print(scissory)      
            print("I chose Scissors")
            print(f"Yes I won because you chose {user.capitalize()}")
        
elif user.lower() == "scissors":
        print(scissory)      
        print("You chose Scissors") 
        if pc == 0:
            print(rocky)      
            print("I chose Rock")
            print(f"Yes I won because you chose {user.capitalize()}")
        elif pc == 1:
            print(papery)      
            print("I chose Paper")  
            print(f"Damn bro I lost because you chose {user.capitalize()}")
        else:
            print(scissory)      
            print("I chose Scissors")
            print(f"Damn, you chose {user.capitalize()}, it's a draw")
