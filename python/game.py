import random
win_number = random.randint(1,100)
geuse = 1
user_input = int(input("please enter your number : "))
game_over = False

while not game_over:
    if user_input == win_number :
        print(f" you win this game in only {geuse} geuse")
        game_over=True
        
    else :
        if win_number > user_input:
            print("you gruse to low number ")
            #  geuse +=1                                 # see we comit this becoz if abow setment got ture 
            #  user_input=int(input("Try agin : "))      # this is DRY technic to reduce code        
        else:
            print("you gruse to hig number ")               
        geuse +=1                                   # if we remove sapce & make in line of if it tahn run     
        user_input=int(input("Try agin : "))        # in else statment & if also 