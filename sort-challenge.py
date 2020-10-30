array = [34, 1 ,9 , 0 , 8, 21, 98, 23, 22, 67, 1230, 897, 7911, 1090, 256, 3500, 478, 21, 4, 2]
#array.sort(reverse= True)
#se declara un arreglo vacio para almacenar los valores en orden
sortedArray=[]
#de declara delete para almacenar la posicion del arreglo que se debe eliminar
delete = 0
#Se declara X para almacenar el valor del numero de iteracion del while
x = 0
#se declara iteracion -1 para eliminar la diferencia entre array e iteracion
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
# se utiliza esta funcion para eliminar la posicion del arreglo
    del(array[delete])
    sortedArray.append(menor)


print(array)
print(sortedArray)
        