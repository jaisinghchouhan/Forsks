def pallindrome(x):
    if int(x)>0:
        if x==x[::-1]:
            return True
        

list1=input("enter numbers").split(" ")
print(any(filter(pallindrome,list1)))
