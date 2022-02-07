# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 10:44:47 2021

@author: thors
"""

mod = 10**9+7
def fibo(n):
    n1,n2 = 1,2
    count = 0
    
    if n ==1:
        return n2%mod
    elif n==2:
        return (n2+n1)%mod
    else:
        while count < n:
            nth = n1+n2
            n1 = n2
            n2 = nth
            count+=1
            
        return n1%mod


num = int(input())
for i in range(num):
    n = int(input())
    print(fibo(n))
    
