# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:24:48 2019

@author: ck069
"""

import random

while True:
    computer=random.randint(1,10)
    #print(computer)
    turn=6
    while True:
        player=int(input("Guess a number between 1 and 10 "))
        #if(player!=int(player)):
         #   print(" enter an integer type value")
        if computer==player:
            print("You win")
            break
        else:
            if computer>player:
                print("too low")
            else:
                print("too high")
        turn=turn-1
        print("turns left {}.".format(turn))
        if turn==0:
            break
    if turn==0:   
        print("you loose")
    #print("secret number is {} any your guess is {}.".format(computer,player))
    print("secret number is {} .".format(computer))
    choice=int(input("press 1 to play again"))
    if choice!=1:
        break