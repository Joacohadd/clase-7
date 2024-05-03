matriz = [[0] * 2 for _ in range(3)]

for i in range(len(matriz)):#Recorre fila x fila
    for j in range(len(matriz[i])):#Recorre columna x columna
        matriz[i] [j] = input("Ingrese un valor: ")


for i in range(len(matriz)):#EL len es cuantas filas tengo
    for j in range(len(matriz[i])):
        print(f"{matriz[i][j]}", end = " ")
    print("")