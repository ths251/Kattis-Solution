# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 12:27:37 2021

@author: thors
"""

while True:
    n, m = map(int, input().split())
    
    if(n == 0 and m == 0):
        break
    
    
    
    heads = []
    for i in range(n):
        heads.append(int(input()))
    heads = sorted(heads)  
        
     
    knights = []
    for i in range(m):
        knight = int(input())
        if knight >= heads[0]:
            knights.append(knight)
    knights = sorted(knights)
    
  
    
    if(len(knights) < n):
        print("Loowater is doomed!")
        continue
    
    
    
    cost = 0
    i = -1
    boolean = False
    for head in heads:
        while i < len(knights):
            i+=1
            if i >= len(knights):
                boolean = True
                break
            if(knights[i]>=head):
               cost+=knights[i]
               break
    
    
  
    
                
    if boolean:
        print("Loowater is doomed!")
        
    else:
        print(cost)
        
    
       


    