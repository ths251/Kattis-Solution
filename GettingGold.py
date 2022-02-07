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

# m dálkar, n línur
m,n = map(int, input().split())

grid = []
rq = Queue()
cq = Queue()
falseD = []
visited = []
gold_counter = 0

for i in range(n):
    dalkur = str(input())
    grid.append([str(j) for j in str(dalkur)])
    falseD = [False]*m
    visited.append(falseD)
    

for i in range(n):
    for j in range(m):
        #Finna starting stöðuna
        if(grid[i][j]=='P'):
            sr = i
            sc = j

rq.enqueue(sr)
cq.enqueue(sc)

#merkja upphafstöðu
visited[sr][sc] = True

dr = [-1,1,0,0]
dc = [0,0,1,-1]


while(rq.size()>0):
    
    
    # ef það er gildra í byrjun
    if((grid[sr][sc+1]=='T') or (grid[sr][sc-1]=='T') or (grid[sr-1][sc]=='T') or(grid[sr+1][sc]=='T')):
        break
    
    r = rq.dequeue()
    c = cq.dequeue()
    
    
    for i in range(len(dr)):
        rr = r+dr[i]
        cc = c+dc[i]
        
        
        #útaf
        if(visited[rr][cc]==True):continue
        #veggur
        if(grid[rr][cc]=='#'): continue
        #gildra
        if(grid[rr][cc]=='T'): continue  
        #gull
        if(grid[rr][cc]=='G'):
            gold_counter+=1 
            grid[rr][cc]='.'
            
        #Ef það er gildra nálægt þá höldum við bara áfram
        if((grid[rr][cc+1]=='T') or (grid[rr][cc-1]=='T') or (grid[rr-1][cc]=='T') or(grid[rr+1][cc]=='T')):
            visited[rr][cc]=True
            continue
  
        visited[rr][cc]=True
        rq.enqueue(rr)
        cq.enqueue(cc)

print(gold_counter)
