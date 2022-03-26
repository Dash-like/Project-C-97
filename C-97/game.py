import random

guess = int(input("Enter Your Guess :-"))
number = random.randint(1, 9)
chances = 0

while chances < 5:
    if not chances < 5:
     print("You Lose!!! The number is", number)
    if number == guess:
        print("Congratulations You WIN!!!")
        break                
    else:
        print("Wrong Guess Try Again!!")
        
        
 
    


