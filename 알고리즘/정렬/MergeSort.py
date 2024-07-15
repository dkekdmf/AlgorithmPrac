import random
def mergesplit(lst):
    medium = int(len(lst)/2)
    if len(lst) <=1:
        return lst
    left= mergesplit(lst[:medium])
    right = mergesplit(lst[medium:])
    return merge(left,right)
    

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