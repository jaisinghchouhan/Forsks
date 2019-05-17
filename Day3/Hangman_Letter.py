import random
def hangman(list):
    while True:
        r=random.randint(0,5) 
        computer = list[r]
        turn=3
        while True:
            player = input("Guess name of a fruit :")
           
            if computer==player:
                print("You win")
                break
            else:
               turn=turn-1
               print("turns left {}.".format(turn))
               if turn==0:
                break
        if turn==0:    
            print("you loose")
        print("name of fruit is is {} .".format(computer))
        choice=int(input("press 1 to play again"))
        if choice!=1:
            break

fruit=["apple","orange","mango","kivi","grapes"]
hangman(fruit)