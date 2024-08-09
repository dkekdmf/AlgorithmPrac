
import random
def quicksort(data):
    if len(data)<=1:
        return data
    left,right = list(),list()
    pivot = data[0]
    
    for i in range(1, len(data)):
        if data[i]<pivot:
            left.append(data[i])
        else:
            right.append(data[i])
    return quicksort(left) + [pivot] + quicksort(right)


def quicksort2(data):
    if len(data)<=1:
        return data
    pivot = data[0]
    left = [item for item in data[1:] if pivot>item]
    right = [item for item in data[1:]if pivot<=item]
    print(left,pivot,right)
    return quicksort2(left) + [pivot] + quicksort2(right)


randlist = random.sample(range(100),20)
print(quicksort2(randlist))


def dfs(graph,startnode):
    visited,needvisited = list(),list()
    needvisited.append(startnode)
    
    while needvisited:
        node = needvisited.pop(0)
        
        for node in graph:
            if node not in visited:
                visited.append(node)
            needvisited.extend(graph(node))
    return visited

# mergesort -> split ---- merge

def mergesplit(lst):
    medium = int(len(lst)/2)
    if len(lst) <=1:
        return lst
    left= mergesplit(lst[:medium])
    right = mergesplit(lst[medium:])
    return merge(left,right)
    


lst1 = [5,4,8,3,2]

def merge(left,right):
    merged = list()
    lp,rp = 0,0
    
    #케이스1: left/right가 남아았을때
    while len(left)>lp and len(right)>rp:
        if left[lp]>right[rp]:
            merged.append(right[rp])
            rp+=1
        else:
            merged.append(left[lp])
            lp+=1
    #케이스2: left만 남아았을때
    while len(left) > lp:
         merged.append(left[lp])
         lp+=1
    #케이스3: right만 남아있을때
    while len(right)>rp:
         merged.append(right[rp])
         rp+=1
    
    return merged
    

    

        
rand = random.sample(range(100),10)
print(mergesplit(rand))