# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 13:58:05 2021

@author: thors
"""

n = int(input())

def isDivisibleNineTimes(n,m):
    #Þarf að gera þá annað fall sem finnur m
    for i in range(9):
        #if there is no remainder
        if(n%m == 0):
            n = n/m
        else:
            return 1
        
    return m
    

def svar(n):
    #128 er stærtsa m sem við getum fengið
    m = 128
    for i in range(m,0,-1):
        tala = i**9
        
        if(n%tala==0):
            return i
    return 1

print(svar(n))
        
        

