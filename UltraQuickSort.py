# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 17:21:03 2021 

@author: thors
"""



n = int(input())
listi = []
for i in range(n):
    a = int(input())
    listi.append(a)
        
sortedListi = sorted(listi)
counter = 0

while(sortedListi!=listi):
    for i in range(1,len(listi)):
        if(listi[i-1]>listi[i]):
            counter+=1
            listi[i-1], listi[i] = listi[i],listi[i-1]
            break   
print(counter)
