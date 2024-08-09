
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
