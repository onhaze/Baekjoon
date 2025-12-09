import sys

student = list(range(1, 31))

for _ in range(28):
    student.remove(int(sys.stdin.readline().rstrip()))

print(sorted(student)[0])
print(sorted(student)[1])