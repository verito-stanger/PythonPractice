array = [34, 1 ,9 , 0 , 8, 21, 98, 23, 22, 67, 1230, 897, 7911, 1090, 256, 3500, 478, 21, 4, 2]
#array.sort(reverse= True)
sortedArray=[]

delete = 0

x = 0
iteration = len(array) - 1
while x <= iteration:
    i = 0
    x+=1
    menor = array[0]
    for lista in array:
        if (lista <= menor):
            menor=lista
            delete = i
        i+=1

    del(array[delete])
    sortedArray.append(menor)


print(array)
print(sortedArray)
        