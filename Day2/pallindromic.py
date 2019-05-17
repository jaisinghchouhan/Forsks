def pallindrome(string):
    if string==string[::-1]:
        return True
    else:
        return False



list1=["12", "9", "61", "5", "14"]

for i in list1:
    if int(i)>0:
        a=pallindrome(str(i))
        if a==True:
            n=True
            break
        else:
            n=False
        
    else:
        print("not integer")
    
if n==True:
    print("true")
else:
    print("false")