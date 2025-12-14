number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N, B = map(int, input().split())
answer = ''

while N:
    answer += number[N % B]
    N//=B

print(answer[::-1])