# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:39:33 2021

@author: thors
"""


P = int(input())


def isPrime(num):
    prime = False
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               prime =False 
               break
       else:
           prime = True  
    else:
       prime = False
    
    return prime
       
def isHappy(num):
    rem=0
    summa=0
    
    while(num>0):
        rem=num%10
        summa +=rem*rem
        num=num//10
        
    return summa


def isHappyAndPrime(num):
    isprime = isPrime(num)
    result = num
    if(isprime==True):
        while(result !=1 and result !=4):
            result = isHappy(result)
        if(result==1):
            return True
        else:
            return False
        
    else:
        return False


for i in range(P):
    yes = 'YES'
    no = 'NO'
    x,y = map(int, input().split())
    if(isHappyAndPrime(y)==True):
        print(f'{x} {y} {yes}')
    else:
        print(f'{x} {y} {no}')
    

