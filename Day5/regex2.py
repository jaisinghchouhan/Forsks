import re
str1=input("enter an email").split(",")
list1=[]
for email in str1:
    if re.findall('[a-z0-9_-]+@\w+\.[a-z]{2,4}',email):
        list1.append(email)
print(list1)        
        