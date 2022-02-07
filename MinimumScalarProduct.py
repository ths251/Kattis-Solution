# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:16:54 2021

@author: thors
"""

X = int(input())
for i in range(X):
    k = i+1
    n = int(input())
    x = [int(x) for x in input().split()]
    y = [int(x) for x in input().split()]
    
    #Til að finna minsta ScalarProduct
    x.sort()
    y.sort(reverse = True)
    
    scalarProd = 0
    for i in range(len(x)):
        scalarProd += x[i]*y[i]
    
    print(f'Case #{k}: {scalarProd}')
