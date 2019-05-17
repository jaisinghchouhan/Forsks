import re
list1=[]
while True:
    cred_num=input("enter card number")
    list1.append(cred_num)
    if not cred_num:
        break

for num in list1:
    if re.findall('[4-6]{1}[0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}',num):
        print("valid")
    else:
        print("invalid")