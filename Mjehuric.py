# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 11:48:43 2021

@author: ths251
"""
#Leið til að fá tölustafina á lista form til að geta vitnað í ákveðin stök
val = list(map(int, input().split()))

#Raða gildinum okkar
valSorted = sorted(val)

while(val !=valSorted):
    if(val[0]>val[1]):
        val[0], val[1] = val[1], val[0]
        print(' '.join(map(str, val)))

    if(val[1]> val[2]):
        val[1], val[2] = val[2], val[1]
        print(' '.join(map(str, val)))

    if(val[2]> val[3]):
        val[2], val[3] = val[3], val[2]
        print(' '.join(map(str, val)))
    
    if(val[3]>val[4]):
        val[3], val[4] = val[4], val[3]
        print(' '.join(map(str, val)))
