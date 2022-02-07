# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 18:46:27 2021

@author: thors
"""

n = int(input())
citations = []
for i in range(n):
    citation = int(input())
    citations.append(citation) 

citations.sort()

def H_index(citations):     
    for i, cited in enumerate(citations):  
        result = len(citations) - i 
        if result <= cited: 
             return result           
    return 0
    
    
print(H_index(citations))

  

