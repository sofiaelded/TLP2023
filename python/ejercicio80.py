padres = []
hijos = []
padresmasdoshijos = 0

for k in range(3):
    pa = input("Ingrese el nombre del padre: ")
    ma = input("Ingrese el nombre de la madre: ")
    padres.append([pa, ma])
    cant = int(input("Ingrese la cantidad de hijos por familia: "))
    hijos.append([])
    for x in range(cant):
        nom = input("Ingrese el nombre del hijo/a: ")
        hijos[k].append(nom)
    
    if cant > 2:
        padresmasdoshijos += 1  

    print("listado del padre, madre y sus hijos ")

for k in range(3):
    print("Padre: ", padres[k][0])
    print("Madre: ", padres[k][1])
    if len(hijos[k]) == 0:
        print(f"El padre {padres[k][0]} y la madre {padres[k][1]} no tienen hijos.")
    for x in range(len(hijos[k])):
        print("Hijos: ", hijos[k][x])

print("Listado de padres y cantidad de hijos que tiene")
for k in range(3):
    print("padre", padres[k][0])
    print("Cantidad de hijos: ", len(hijos[k]))

print(f"Total de familias con más de 2 hijos: {padresmasdoshijos}")

