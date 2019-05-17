str1=input("enter an string")
count1=0
count2=0
for i in str1:
    if i.isalpha():
        count1=count1+1
    elif i.isdigit():
        count2=count2+1
    else:
        continue
print(count1)
print(count2)
