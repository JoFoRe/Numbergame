import numpy as np
from random import randint



# Number game with a counter and some defined messages for low attempt counts

def NumberGame():
    count = 0
    bounds = int(input("Select your upper bound: "))
    solution = randint(0,bounds)
    guess = input("Choose any number between 0 and "+ str(bounds) + ". What number is your guess? ")  
    while guess != solution:
        if float(guess) > solution:
            print("too high try again")
            guess = input("try again")
            count +=1

        if float(guess) < solution:
            print ("too low try again")
            guess = input("try again")
            count +=1

        if float(guess) == solution:
            count +=1
            print("Right on! Number " + str(solution) +", is correct! It only took you: " + str(count) +" attempts.")
            if count < 4:
                print("Thats pretty damn good!")
            if count == 1:
                print("But one attempt huh. That is sus.")
            break

        
NumberGame()