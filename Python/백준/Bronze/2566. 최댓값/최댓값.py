A, B = [], []

for i in range(9):
    a = list(map(int, input().split()))
    b = max(a)
    A.append(a)
    B.append(b)
    
row = B.index(max(B))
col = A[row].index(max(B))

print(max(B))
print(row + 1, col + 1)