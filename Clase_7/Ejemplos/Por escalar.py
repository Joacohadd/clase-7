matriz = [ #3x4
    [5,9,7,10], 
    [1,1,8,72], 
    [8,7,9,14]  
]

escalar = 3

matriz_producto = [[0] * len(matriz[0]) for _ in range(len(matriz))]

for i in range(len(matriz_producto)):
    for j in range(len(matriz_producto[i])):
        matriz_producto[i][j] = matriz [i][j] * escalar



for i in range(len(matriz)):#EL len es cuantas filas tengo
    for j in range(len(matriz[i])):
        print(f"{matriz_producto[i][j]}", end = " ")
    print("")