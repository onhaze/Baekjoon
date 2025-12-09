A, B = input().split()
A = int(A[::-1])
B = int(B[::-1])

if A < B:
    print(B)
else:
    print(A)