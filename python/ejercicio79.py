empleados = []
faltas = []
cantfaltantes=0
for k in range(3):
    nombre = input("Ingrese el nombre del empleado: ")
    empleados.append(nombre)
    cant= int(input("Cuantas faltas tiene: "))
    faltas.append([])
    for x in range(cant):
        dia=int(input("Ingrese el número del día que faltó: "))
        faltas[k].append(dia)
print("Nombre de empleado y días que faltó ")
for k in range(3):
    print(empleados[k])
    for x in range(len(faltas[k])):
        print (faltas[k][x])
print("Nombres de empleados y cantidad de inasistencias mayores a 10: ")
for x in range(3):
    print(empleados[x],len(faltas[x]))
for x in range(1,3):
    if len (faltas[x])>10:
        cantfaltantes=cantfaltantes+1
print("Empleado/s que faltaron menos a 3: ")
for x in range(3):
    if len (faltas[x])<3:
        print(empleados[x])
print("Empleado/s que faltaron mmas de 10 veces: ",cantfaltantes)   

