# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:58:14 2019

@author: ck069
"""

num=0
while num<100:
    num=num+1
    if num%3==0 and num%5==0:
        print("fizz buzz")
    elif num%5==0:
        print("buzz")
    elif num%3==0:
        print("fizz")
    else:
        print(num)
        
    