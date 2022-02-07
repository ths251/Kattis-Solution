# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 13:07:47 2021

@author: thors
"""

n = int(input())

weights = []

for i in range(n):
    weight = int(input())
    weights.append(weight)
target = 1000   
weights.sort(reverse = True)

#Lengd 1
if(len(weights)==1):
    summa = sum(weights)
    print(summa)


else: 
    summur = []
    lokagildi = 0
    nta = len(weights)
    for i in range(nta):
        summa1 = weights[i] 
        for j in range(1+i, nta):
            
            if(abs(summa1- target) < abs((summa1+weights[j])-target)):
                summa1 = summa1 
            else:
                summa1 += weights[j]
        
        summur.append(summa1)
          
    lokagildi = summur[0]
    for i in range(1,len(summur)):
        if(abs(lokagildi-target) < abs(summur[i]-target)):
            lokagildi = lokagildi
        else:
            lokagildi = summur[i]
            
            
    print(lokagildi)
        
    
