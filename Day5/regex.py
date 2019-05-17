import re
str1=input("enter an string").split(",")
for val in str1:
    if re.findall('[+-]?[0-9]*\.[0-9]+',val):
        print("true")
    else:
        print("false")
