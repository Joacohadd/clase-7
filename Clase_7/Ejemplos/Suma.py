matriz_a = [ #3x4
    [5,9,7,10], 
    [1,1,8,72], 
    [8,7,9,14]  
]

matriz_b = [ #3x4
    [5,9,7,10], 
    [1,1,8,72], 
    [8,7,9,14]  
]


matriz_suma = [[0] * len(matriz_a[0]) for _ in range(len(matriz_a))]

for i in range(len(matriz_suma)):
    for j in range(len(matriz_suma[i])):
        matriz_suma[i][j] = matriz_a [i][j] + matriz_b [i][j]
        
        
for i in range(len(matriz_suma)):#EL len es cuantas filas tengo
    for j in range(len(matriz_suma[i])):
        print(f"{matriz_suma[i][j]}", end = " ")
    print("")