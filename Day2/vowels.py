# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:36:11 2019

@author: ck069
"""
states=input("enter the names of cities").split(" ")
vowels=('A','a','E','e','I','i','O','o','U','u')
output=[]
for items in states:
    new_state=''
    for char in items:
        if char not in vowels:
            new_state=new_state+char
    output.append(new_state)
print(output)    