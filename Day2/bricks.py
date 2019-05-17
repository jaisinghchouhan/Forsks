def bricks(small,big,total):
    if small+big*5>=total:
        if total%5<=small:
            return True
        else:
            return False
    else:
        return False
    
    
small=int(input("enter total number of one intch of brick"))
large=int(input("enter the number of 5 intch of brick"))
total=int(input("enter the total length of brick to be built"))
print(bricks(small,large,total))