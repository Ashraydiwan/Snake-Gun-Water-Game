import random

def gameWin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you=='g':
            return True 
    elif comp == 'w':
        if you =='g':
            return False
        elif you =='s':
            return True 

randomno = random.randint(1,3)
print(randomno)
if randomno == 1:
    comp = 's'
elif randomno == 2:
    comp = 'w'
elif randomno == 3:
    comp = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(comp,you)
if a == None:
    print("the game is tie")
elif a:
    print("you win")
else:
    print("you lose")
