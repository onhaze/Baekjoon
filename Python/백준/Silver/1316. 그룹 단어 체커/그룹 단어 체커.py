n = int(input())
count = 0

for _ in range(n):
    word = input()
    is_group_word = True
    
    for j in range(len(word)):
        if j > 0 and word[j] != word[j-1]:
            if word[j] in word[:j]:
                is_group_word = False
                break

    if is_group_word:
        count += 1

print(count)