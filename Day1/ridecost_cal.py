# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:01:34 2019

@author: ck069
"""
travel=float(input("Enter the total distance travel in a day"))
cost=float(input("Enter the cost diseal per liter"))
average=float(input("Enter the average of vehicle"))
total_cost=(travel/average)*cost
print(total_cost)
