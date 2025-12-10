a = input().lower()
b = list(set(a))
c_li = []

for i in range(len(b)):
    c = a.count(b[i])
    c_li.append(c)
    
if c_li.count(max(c_li)) > 1:
    print('?')
else:
    print(b[c_li.index(max(c_li))].upper())