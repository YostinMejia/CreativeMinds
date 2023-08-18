# función n impar
def print_diagonal_zigzag_IMP(matrix):
    n = len(matrix)
    result = []

    for i in range(n):
        indexes = range(i, -1, -1) if i % 2 == 0 else range(0, i + 1)
        result.extend(matrix[j][i - j] for j in indexes)
    for i in range(1, n):
        indexes = range(n - 1, i - 1, -1) if i % 2 == 0 else range(i, n)
        result.extend(matrix[j][i + n - j - 1] for j in indexes)

    print(", ".join(map(str, result)))

# función n par
def print_diagonal_zigzag(matrix):
    n = len(matrix)
    result = []

    for i in range(n):
        indexes = range(i, -1, -1) if i % 2 == 0 else range(0, i + 1)
        result.extend(matrix[j][i - j] for j in indexes)

    for i in range(1, n):
        indexes = range(i, n) if i % 2 == 0 else range(n - 1, i - 1, -1)
        result.extend(matrix[j][i + n - j - 1] for j in indexes)

    print(", ".join(map(str, result)))


def main():
    n = int(input("Ingrese el valor de n para la matriz nxn: "))
    matrix = [[i * n + j + 1 for j in range(n)] for i in range(n)]
    print("Matriz generada:")
    for row in matrix:
        print(row)
    print("\nElementos en diagonal zigzag:")
    if n % 2 == 0:
      print_diagonal_zigzag(matrix)
    else:
      print_diagonal_zigzag_IMP(matrix)

if __name__ == "__main__":

    main()
