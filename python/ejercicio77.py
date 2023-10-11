lista=[]
elementos=int(input("Cuántos elementos tendrá la lista: "))
sub=int(input("Cuántos elementos tendrán las listas internas: "))
for k in range (elementos):
    lista.append([])
    for x in range(sub):
        valor=int(input("Ingrese valor: "))
        lista[k].append(valor)
print(lista)
suma=0
for k in range (len(lista)):
    for x in range(len(lista[k])):
       suma=suma+lista[k][x]
print("La suma de todos los elementos",suma)
multiplicacion=1
for k in range (len(lista)):
    for x in range(len(lista[k])):
       multiplicacion=multiplicacion*lista[k][x]
print("La multiplicación de todos los elementos",multiplicacion)
division=0
division=multiplicacion/suma
print("La división de la multiplicación sobre la suma es de: ",division)
