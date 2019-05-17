str1=input("enter an string")
dic1={}
for i in str1:
    if i in dic1:
        dic1[i]=dic1[i]+1
    else:
        dic1[i]=1
print(dic1)