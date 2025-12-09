import sys

N = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
M = max(M_list)

for i in range(N):
    M_list[i] = M_list[i]/M*100

print(sum(M_list)/N)