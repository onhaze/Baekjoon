dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0

word = input()

for i in range(len(word)):
    for j in dial:
        if word[i] in j:
            result = result + dial.index(j) + 2
            
print(result+len(word))