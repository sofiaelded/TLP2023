padres=[]
hijos=[]
for k in range(3):
    pa=input("Ingrese el nombre del padre: ")
    ma=input("Ingrese el nombre de la madre: ")
    padres.append ([pa,ma])
    cant=int(input("Ingrese la cantidad de hijos por familia: "))
    hijos.append([])
    for x in range(cant):
        nom=input("Ingrese el nombre del hijo/a: ")
        hijos[k].append(nom)
    print("listado del padre,madre y sus hijos ")
for k in range(3):
    print("Padre: ", padres [k][0])
    print("Madre: ", padres [k][1])
    for x in range(len(hijos[k])):
        print("Hijos: ",hijos[k][x])
print("Listado de padres y cantidad de hijos que tiene")
for k in range(3):
    print("padre",padres[k][0])
    print("Cantidad de hijos: ",len(hijos[k]))
