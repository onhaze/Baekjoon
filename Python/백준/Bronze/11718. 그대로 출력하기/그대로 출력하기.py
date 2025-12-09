S_list = []
i = 0
while True:
    try:
        S_list.append(input())
        i += 1
    except:
        break

for j in range(i):
    print(S_list[j])