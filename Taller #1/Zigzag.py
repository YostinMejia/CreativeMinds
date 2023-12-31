def print_diagonal_zigzag_IMP(matrix):    # O(n^2)
    n = len(matrix)    # O(1)
    result = []        # O(1)

    for i in range(n):    # O(n^2)
        indexes = range(i, -1, -1) if i % 2 == 0 else range(0, i + 1)    # O(n^2)
        result.extend(matrix[j][i - j] for j in indexes)    # O(n^2)
    for i in range(1, n):    # O(n^2)
        indexes = range(n - 1, i - 1, -1) if i % 2 == 0 else range(i, n)    # O(n^2)
        result.extend(matrix[j][i + n - j - 1] for j in indexes)    # O(n^2)

    print(", ".join(map(str, result)))    # O(1)
    
# Suma complejidad: 3 O(1)+ 6 O(n^2)
def print_diagonal_zigzag(matrix):    # O(n^2)
    n = len(matrix)    # O(1)
    result = []    # O(1)

    for i in range(n):    # O(n^2)
        indexes = range(i, -1, -1) if i % 2 == 0 else range(0, i + 1)    # O(n^2)
        result.extend(matrix[j][i - j] for j in indexes)    # O(n^2)

    for i in range(1, n):    # O(n^2)
        indexes = range(i, n) if i % 2 == 0 else range(n - 1, i - 1, -1)    # O(n^2)
        result.extend(matrix[j][i + n - j - 1] for j in indexes)    # O(n^2)

    print(", ".join(map(str, result)))    # O(1)

# Suma complejidad: 3 O(1)+ 6 O(n^2)

def main():    # O(n^2)
    n = int(input("Ingrese el valor de n para la matriz nxn: "))    # O(1)
    matrix = [[i * n + j + 1 for j in range(n)] for i in range(n)]        # O(n^2)
    print("Matriz generada:")        # O(1)
    for row in matrix:    # O(n)
        print(row)    # O(n)
    print("\nElementos en diagonal zigzag:")    # O(1)
    if n % 2 == 0:    # O(1)
      print_diagonal_zigzag(matrix)    # O(1)
    else:    # O(1)
      print_diagonal_zigzag_IMP(matrix)    # O(1)

# Suma complejidad: 6 O(1)+ 2 O(n) +O(n^2)

if __name__ == "__main__":        # O(1)
    main()        # O(1)

# Suma complejidad: 2 O(1)
