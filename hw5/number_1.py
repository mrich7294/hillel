import sys

numb = int(input('Введіть число: '))
lst = []
count = 0
while numb > 0:
    lst.append(numb % 10)
    numb = numb // 10
    # lst.sort()
    k = len(lst)
# print(lst)
for i in range(0, k):
    for j in range(0, k):
        if lst[i] == lst[j]:
            if i == j:
                continue
            else:
                print("YES", lst[i], lst[j])
                sys.exit()
print("NO")
