"""a = 50
b ='100.1'
print(a+int(a))  

print(type(a))
print(type(b))"""

array = [23, 4 , 'Vero', 12.3,{'Vero': '95802122', 'Mikey': '19092838'}] 
print(array[4]['Mikey'])
array.append(2)
array[4]['Mikey']= ['Modified', 'Unmodified']
for a in array:
    print(a)

