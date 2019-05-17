str1=input("enter a string")
str2="abcdefghijklmnopqrstuvwxyz"
count=0
if len(str1)>=26:
    for i in range(0,26):
        if str2[i] in str1:
            count=count+1
            continue
        else:
            break
if count==26:
    print("pangram")
else:
    print("not pangarm")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    