# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 22:21:57 2021

@author: thors
"""

class Queue:
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0,item)
        
        
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
#sr sc er starting, er,ec er ending
n, m = map(int, input().split())
     
grid = []


for i in range(n):
    k = str(input())
    grid.append([str(j) for j in str(k)])    
    
def binary(sr,sc,er, ec, grid, n,m):
    rq = Queue()
    cq = Queue()
    
    
    if(grid[sr][sc]=='1'):
        return 0
    
    falseD = []
    visited = []
    
    for i in range(n):
       falseD = [False]*m
       visited.append(falseD)     
    
    reached_end = False
    rq.enqueue(sr)
    cq.enqueue(sc)
    visited[sr][sc] = True
    
    dr = [-1, 1, 0,0]
    dc = [0,0,1,-1]
    
    while(rq.size()>0):
        r = rq.dequeue()
        c = cq.dequeue()

        if(r==er and c == ec):
            reached_end = True
            break
        
        for i in range(len(dr)):
            rr = r+dr[i]
            cc = c+dc[i]
            
            if(rr <0 or cc < 0): continue
            if(rr>= n or cc>=m): continue
        
            if(grid[rr][cc]=='1'):
                continue
            
            if(visited[rr][cc]==True):continue
        
            rq.enqueue(rr)
            cq.enqueue(cc)
            visited[rr][cc]=True
            
    if(reached_end):
        return 1
    else:
        return 0

def decimal(sr,sc,er, ec,grid,n,m):
    
    rq = Queue()
    cq = Queue()
    
    if(grid[sr][sc]=='0'):
        return 0
    falseD = []
    visited = []
    
    for i in range(n):
       falseD = [False]*m
       visited.append(falseD)      
    
    reached_end = False
    rq.enqueue(sr)
    cq.enqueue(sc)
    visited[sr][sc] = True
    
    dr = [-1, 1, 0,0]
    dc = [0,0,1,-1]
    
    while(rq.size()>0):
        r = rq.dequeue()
        c = cq.dequeue()
        
        
        if(r==er and c == ec):
            reached_end = True
            break
        
        for i in range(len(dr)):
            rr = r+dr[i]
            cc = c+dc[i]
            
            if(rr <0 or cc < 0): continue
            if(rr>= n or cc>=m): continue
        
            if(grid[rr][cc]=='0'):continue
            if(visited[rr][cc]==True):continue
        
            rq.enqueue(rr)
            cq.enqueue(cc)
            visited[rr][cc]=True
    if(reached_end):
        return 1
    else:
        return 0
    
query = int(input())
for i in range(query):
    r1,c1,r2,c2 = map(int, input().split())
    if(binary(r1-1,c1-1,r2-1,c2-1,grid,n,m)==1):
        print('binary')
    elif(decimal(r1-1,c1-1,r2-1,c2-1,grid,n,m)==1):
        print('decimal')
    else:
        print('neither')

    