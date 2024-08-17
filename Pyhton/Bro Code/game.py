#       rock , paper, scissors game

import random 
def rps_game() :
    while True : 
        choises =  ['rock' , 'paper' ,'scissors']
        computer =  random.choice(choises)
        player = None
        while player not in choises : 
            player = input("rock , paper or scissors ? ").lower()

        print("computer : " , computer)
        print("player   : " , player)
        if computer == player : 
            print("you won!") 
        else : 
            print("ypu lose!")    

        if input("play again ? ").lower() not in ('yes' , 'y') : 
            break

    print("Bye!")