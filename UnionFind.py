# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 19:38:08 2021

@author: thors
"""
#N mörg stök 
#Q margar aðgerðir
N, Q = map(int, input().split())

#tolurListi = list(range(0, N-1))
unionListi = []

def union(a,b):
    unionListi.append(a)
    unionListi.append(b)
    return None


def find(a,b):
    if(a==b):
        print('yes')
        
    elif a and b in unionListi:
        print('yes')
    else:
        print('no')

        
for i in range(Q):
    oper, a,b = input().split()
    
    if(oper == '='):
        union(a,b)
        
    elif(oper == '?'):
        find(a,b)
        
    else:
        break
        

        


