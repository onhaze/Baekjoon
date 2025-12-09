import sys

N, M = map(int, sys.stdin.readline().split())
basket = [0]*N

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for n in range(i-1, j):
        basket[n] = k
        
for a in range(N):
    print(basket[a], end=" ")