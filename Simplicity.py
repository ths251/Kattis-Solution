# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 13:42:02 2021

@author: thors
"""

strengur = input()
Letters = set(strengur)
counter = []

for i in Letters:
    counter.append(strengur.count(i))
   
counter.sort()

if len(Letters) < 3:
    print("0")
else:
    print(sum(counter) - sum(counter[-2:]))

    