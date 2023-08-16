def MatrizHorizontal (matriz, fila=0, columna=0, suma=1):
    if fila == len(matriz):
        return
    
    if columna == len(matriz[0]):
        return MatrizHorizontal(matriz, fila+1, columna-1, -1)
    elif columna ==-1:
        
        return MatrizHorizontal(matriz, fila+1, columna+1, 1)
    print(matriz[fila][columna])
    columna+=suma

    return MatrizHorizontal(matriz, fila, columna, suma)

def main():
    a =[]
    c = 0
    n = int(input("Ingrese la cantidad de filas de la matriz ->"))
    m = int(input("Ingrese la cantidad de columnas de la matriz ->"))
    for i in range(n):
        l=[]
        for j in range(m):
           l.append(c) 
           c+=1
        a.append(l)

    for i in a:
        print(i)

    MatrizHorizontal(a)

main()