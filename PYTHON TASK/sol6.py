rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
A = []
B = []
print("Enter elements of Matrix A:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    A.append(row)
print("Enter elements of Matrix B:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    B.append(row)
C = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    C.append(row)
print("Resultant Matrix:")
for row in C:
    print(row)