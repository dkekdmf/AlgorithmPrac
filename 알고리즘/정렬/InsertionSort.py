import random


data_list = random.sample(range(100),10)

def insertionsort(data):
    for index in range(len(data)-1):
        for index2 in range(index+1,0,-1):
            if data[index2]<data[index2-1]:
                data[index2],data[index2-1] = data[index2-1],data[index2]
            else:
                break
    return data
print(insertionsort(data_list))