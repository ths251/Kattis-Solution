# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:27:33 2021

@author: thors
"""

m,n = map(int, input().split())

def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)

cut = gcd(m,n)
if(((m//cut)%2==0) or ((n//cut)%2==0)):
    print(0)
else:
    print(cut)
    
#cut = gcd(m,n)
#m /=cut
#n /=cut
#if(m%2==0 or n%2==0):
 #   cut = 0

#print(cut)