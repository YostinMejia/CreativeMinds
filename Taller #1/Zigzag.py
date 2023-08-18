# función n impar
def print_diagonal_zigzag_IMP(matrix):    # O(n)
    n = len(matrix)    # O(1)
    result = []        # O(1)

    for i in range(n):    # O(n)
        indexes = range(i, -1, -1) if i % 2 == 0 else range(0, i + 1)    # O(n)
        result.extend(matrix[j][i - j] for j in indexes)    # O(n)
    for i in range(1, n):    # O(n)
        indexes = range(n - 1, i - 1, -1) if i % 2 == 0 else range(i, n)    # O(n)
        result.extend(matrix[j][i + n - j - 1] for j in indexes)    # O(n)

    print(", ".join(map(str, result)))    # O(1)

# función n par
def print_diagonal_zigzag(matrix):    # O(n)
    n = len(matrix)    # O(1)
    result = []    # O(1)

    for i in range(n):    # O(n)
        indexes = range(i, -1, -1) if i % 2 == 0 else range(0, i + 1)    # O(n)
        result.extend(matrix[j][i - j] for j in indexes)    # O(n)

    for i in range(1, n):    # O(n)
        indexes = range(i, n) if i % 2 == 0 else range(n - 1, i - 1, -1)    # O(n)
        result.extend(matrix[j][i + n - j - 1] for j in indexes)    # O(n)

    print(", ".join(map(str, result)))    # O(1)


def main():    # O(n)
    n = int(input("Ingrese el valor de n para la matriz nxn: "))    # O(1)
    matrix = [[i * n + j + 1 for j in range(n)] for i in range(n)]        # O(n)
    print("Matriz generada:")        # O(1)
    for row in matrix:    # O(n)
        print(row)    # O(n)
    print("\nElementos en diagonal zigzag:")    # O(1)
    if n % 2 == 0:    # O(1)
      print_diagonal_zigzag(matrix)    # O(1)
    else:    # O(1)
      print_diagonal_zigzag_IMP(matrix)    # O(1)

if __name__ == "__main__":        # O(1)
    main()        # O(1)
