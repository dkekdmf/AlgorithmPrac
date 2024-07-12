N = int(input())
lst = list(map(int,input().split()))
M = int(input())
lst2 = list(map(int,input().split()))
lst.sort()
for i in lst2: 
    l,r = 0,N-1 
    isExist = False
    while l<=r:
        m = (l+r)//2
        if i == lst[m]:
            isExist = True
            print(1)
            break
        elif i>=lst[m]:
            l = m+1
        elif i<=lst[m]:
            r = m-1
    if not isExist:
        print(0)
        




# def isExist(arr,x):
#     l,r = 0,len(arr)-1
#     while l<=r:
#         m = (l+r)/2
#         if arr[m]<x: l =m+1
#         elif arr[m]>x: r = m-1
#         else: return True
#     return False
