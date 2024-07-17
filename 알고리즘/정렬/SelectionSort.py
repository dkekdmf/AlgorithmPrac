import random
n = 10
array = random.sample(range(100),10)

def Selec(data):
    for i in range(len(data)):
        min_index = i
        for j in range(i+1,len(data)):
            if data[min_index]>data[j]:
                min_index = j
        data[i],data[min_index] = data[min_index],data[i]
    return data
print(Selec(array))