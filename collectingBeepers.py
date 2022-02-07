# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 08:06:50 2021

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
    
scenarios = int(input())


 
def findingBeepers(sr,sc,er,ec, grid, n,m):
    
    #Búa til visited hér
    
    #Movecount endurstillt alltaf fyrir hverja leit
    move_count = 0
    nodes_left_in_layer = 1
    nodes_in_next_layer = 0

    reached_end = False
    rq = Queue()
    cq = Queue()

    rq.enqueue(sr)
    cq.enqueue(sc)
    falseD = []
    visited = []
    for i in range(n):
       falseD = [False]*m
       visited.append(falseD) 
    
    
    visited[sr][sc] = True
    while(rq.size() >0):
        r = rq.dequeue()
        c = cq.dequeue()
        
        if(r==er and c ==ec):
            reached_end = True
            break
        
        dr = [-1,1,0,0]
        dc = [0,0,1,-1]
        
        for i in range(len(dr)):
        
            rr = r+dr[i]
            cc = c+dc[i]
            
            if(rr <0 or cc < 0): continue
            if(rr>= n or cc>=m): continue
            
            if(visited[rr][cc]==True):continue
         
            rq.enqueue(rr)
            cq.enqueue(cc)
            visited[rr][cc]=True
            nodes_in_next_layer+=1
            
        nodes_left_in_layer-=1
        if(nodes_left_in_layer==0):
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count+=1
        
    if reached_end:
        return move_count
        
    else:
        return 0

for i in range(scenarios):
    counter = 0
    startingI = []
    startingJ = []
    n, m = map(int, input().split()) #n,m
    sr,sc = map(int, input().split()) #starting
    grid = []
    gridDalkur = []
    for j in range(n):
       gridDalkur = [*range(1,m+1)]
       grid.append(gridDalkur)

    
    beepers = int(input()) #beepers
    for k in range(beepers):
        er,ec = map(int, input().split())
        startingI.append(er)
        startingJ.append(ec)

    
    counter+=findingBeepers(sr-1, sc-1, startingI[0]-1,startingJ[0]-1, grid,n,m)
    for x in range(1,beepers):
        counter+=findingBeepers(startingI[x-1]-1, startingJ[x-1]-1, startingI[x]-1,startingJ[x]-1, grid,n,m)
    counter+=findingBeepers(startingI[beepers-1]-1, startingJ[beepers-1]-1, sr-1,sc-1, grid,n,m)
    print(counter)
        