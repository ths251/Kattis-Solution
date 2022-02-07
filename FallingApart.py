# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 19:06:59 2021

@author: thors
"""

n = int(input())
a = [int(x) for x in input().split()]

a.sort(reverse = True)

Alice = 0
Bob = 0
for i in range(0, len(a), 2):
    Alice += a[i]

for i in range(1, len(a), 2):
    Bob+= a[i]


print(Alice ,Bob)