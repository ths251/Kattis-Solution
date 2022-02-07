# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 11:27:33 2021

@author: ths251
"""
val = input()
print(val[0], end = "")
for i in range(len(val)):
    if(val[i]=="-"):
        print(val[i+1], end= "")
        
