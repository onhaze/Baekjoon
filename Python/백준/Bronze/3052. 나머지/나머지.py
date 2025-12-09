import sys

listA = []

for _ in range(10):
    listA.append((int(sys.stdin.readline().strip())) % 42)

listB = set(listA)   
print(len(listB))