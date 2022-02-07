# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:13:49 2021

@author: thors
"""
N = int(input())
   
def subsets(n):
    subs=0
    if(n==0 or n==1):
        return 0
    else:
        subs = 2**n-n-1
    return subs

print(subsets(N))