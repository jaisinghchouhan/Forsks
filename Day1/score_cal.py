# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:17:09 2019

@author: ck069
"""
A1 = float(input("Enter the marks of assignments 1 :"))
A2 = float(input("Enter the marks of assignments 2 :"))
A3 = float(input("Enter the marks of assignments 3 :"))
E1 = float(input("enter the marks of exam 1"))
E2 = float(input("enter the marks of exam 2"))

weighted_score= (A1+A2+A3)*0.1 +(E1+E2)*0.35

print(weighted_score)

