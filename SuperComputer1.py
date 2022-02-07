# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 14:17:44 2021

@author: thors
"""

class FenwickTree:
    def __init__(self, n):
        self.arr = [False]*n
        self.n = n
        self.sum_tree = [0] * (self.n + 1)

    def BITTree(self, i):
        value = -1 if self.arr[i-1] else 1
        #self.arr[i-1] = not self.arr[i-1]
        while i <= self.n:
            self.sum_tree[i] += value
            i += i & (-i)

    def sums(self, l, r):
        l = self.sum(l-1) if l > 1 else 0
        r = self.sum(r)
        return r-l
    
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.sum_tree[i]
            i -= i & (-i) 
        return s

def main():
    N,Q= map(int,input().split())
    ft = FenwickTree(N)
    for i in range(Q):
        n = input().split()
        if n[0] == 'F':
            ft.BITTree(int(n[1]))
        if n[0] == 'C':
            l = int(n[1])
            r = int(n[2])
            print(ft.sums(l,r))

if __name__ == "__main__":
    main()