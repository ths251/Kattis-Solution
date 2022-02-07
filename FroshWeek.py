# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 11:38:36 2021

@author: thors
"""


def mergeSort(arr):
    if len(arr) > 1:
 
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
 
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
            
N = int(input())
array1 = []
count = 0
for i in range(N):
    n = int(input())
    array1.append(n)

mergeSort(array1)
print(count)


