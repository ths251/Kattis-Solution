# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 12:01:28 2021

@author: thors
"""

booGildi = True

while(booGildi == True):
    counter = 0
    summa = 0
    k = 1
    n = int(input())
    
    if(n == 0):
        booGildi = False
        break
    
    i = 0
    while(i<k):
        if(n <=summa + (i+1)):
            print(counter)
            break
        else:
            k+=1
            counter=i+1
            summa+=i
        i+=1
            
    