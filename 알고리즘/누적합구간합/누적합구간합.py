
N,M = map(int,input().split())
arr = [0]+list(map(int,input().split()))
acc = [0]*(N+1)
for i in range(1,N+1):
    acc[i] = acc[i-1]+ arr[i]
    
for _ in range(M,0,-1):
    s,c = map(int,input().split())
    print(acc[c]-acc[s-1])