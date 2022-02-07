# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 12:49:50 2021

@author: thors
"""

n = int(input())

t = [int(x) for x in input().split()]


t.sort(reverse = True)

days = 1
maxDays = t[0]+days

for i in range(1, len(t)):
       days+=1
       if(t[i]+days > maxDays):
           maxDays = t[i]+days
           
party = maxDays+1

print(party)
           
    
