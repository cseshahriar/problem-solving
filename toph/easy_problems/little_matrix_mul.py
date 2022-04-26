""" matrix multiplication not solved"""
row = int(input())
column = int(input())
c = column//2

def make_matrix(row: int, col: int):
    matrix = []
    for _ in range(row):
        for _ in range(c):
            a = list(map(int, input().split()))
        matrix.append(a)
    return matrix


X = make_matrix(row, column)
Y = make_matrix(row, column)

result = [
    [sum(a*b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)]
    for X_row in X
]
for r in result:
    print(r)
