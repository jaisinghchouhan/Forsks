# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:51:12 2019

@author: ck069
"""
str1 = "RESTART"
print(str1)
loc = str1.find('R')
str2 = str1[loc+1:]
print(str1[0:loc+1]+str2.replace('R','$'))




