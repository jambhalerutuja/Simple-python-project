import random

#Snake Water Gun
def gameWin(computer,You):
    #If two values are equal,declare tie!
    if computer==You:
        return None

    #Check for all posibilities when computer choose s
    elif computer == 's':
        if You=='w':
            return False
        elif You=='g':
            return True
            
        
    #Check for all posibilities when computer choose w
    elif computer == 'w':
        if You=='g':
            return False
        elif You=='s':
            return True
    
    #Check for all posibilities when computer choose g
    elif computer == 'g':
        if You=='s':
            return False
        elif You=='w':
            return True

#First part of game that will be visible on output screen       
print("Computer Turn: Snake(s) Water(w) or Gun(g)??")
rand_no=random.randint(1,3)
if rand_no == 1:
    computer='s'
elif rand_no == 2:
    computer='w'
elif rand_no == 3:
    computer='g'

#Second part of game that will be visible on output screen 
You=input("Your Turn : Sanke(s) Water(w) Gun(g)??")
x=gameWin(computer,You)

print(f"Computer chooses {computer}")
print(f"You chooses {You}")

#Final part 
if x == None:
    print("The Game Is Tie!")
elif x:
    print("You Win :)")
else:
    print("You Lose :(")