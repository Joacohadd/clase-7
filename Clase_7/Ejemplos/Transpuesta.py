matriz = [ #3x4
    [5,9,7,10], #0
    [1,1,8,72], #1
    [8,7,9,14]  #2
]

for j in range(len(matriz[0])):
    for i in range(len(matriz)):
        print(f"{matriz[i][j]:4}", end = " ") #El :4 es visual en consola
    print("")