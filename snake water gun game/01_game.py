#                          Made by Md kashif Alam

# (Snake Water gun game)    or   (Rock Paper Scissor game) 

import random
def winner(cpu, you):
    if cpu == you:   # all possibilities
        return None
    
    elif cpu == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    
    elif cpu == "w":
        if you == "g":
            return False
        elif you == "s":
            return True

    elif cpu == "g":
        if you == "w":
            return True
        elif you == "s":
            return False

print("CPU Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1,3)
if randNo == 1:
    cpu = "s"
elif randNo == 2 :
    cpu = "w"
elif randNo == 3:
    cpu = "g"

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = winner(cpu, you)

print(f"CPU choose {cpu}")
print(f"You choose {you}")

if a == None:
    print("The game is draw!")
elif a:
    print("You win!")
else:
    print("You lose!")



