#----Conditions----
# Operators
#Variables
Integer = 10
Float = 0
String = "Mikey"
Boolean = False
Array = [1, 3, 4, 8, 76]
Dictionary = {'Papagayo':'objeto', 'Patilla':'fruta'}
Tuple = (12,25)
Array2 =[]

#validation = type(Tuple)
"""if (Integer <= 10):
    print("Si es menor a 10")
if (Boolean):
    print("Boolean es VERDADERO!!")
else:
    print("Esa Vaina es FALSA!!")"""

if(Float == 1):
    print("El Valor es muy bajo!!")
elif (Float > 1 and Float < 5): #elif es un posible sustituto del switch case
    print("Todavia te falta mi ciela!")
elif(Float > 4 and Float < 15):
    print("Pelo a pelo menol!")
else:
    print("Esta vaina no aplica!")

if (String is not None):  #not None = No es Nulo
    print(String)

if (len(Array2) != 0):
    print("No hay nada adentro!")





