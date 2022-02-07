
def root(p, a):
    while(p[a]>=0):
        a = p[a]
    return a



def Union(p, a, b):
    rootA = root(p,a)
    rootB = root(p,b)
    if(rootA==rootB):
        return
    p[rootA]+=p[rootB]
    p[rootB]+=rootA
    

def size(p, a):
    return -p[root(p,a)]

def main():
    N,Q= map(int,input().split())
    
    listi = list(range(0,N))
    
    
    for i in range(Q):
        n = input().split()
        if(n[0]=='t'):
            Union(listi, int(n[1])-1, int(n[2])-1)
        else:
            print(size(listi, int(n[1])-1))
    
    
if __name__ == "__main__":
    main()