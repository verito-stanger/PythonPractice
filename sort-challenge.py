array = [34, 1 ,9 , 0 , 8, 21, 98, 23, 22, 67, 1230, 897, 7911, 1090, 256, 3500, 478, 21, 4, 2]
#array.sort(reverse= True)
print(array)
sortedArray=[]
i= 1
menor= 0
for lista in array:
    if (lista <= array[i]):
        menor=lista
sortedArray.append(menor)
print(sortedArray)
        