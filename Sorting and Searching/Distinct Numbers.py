n = int(input())
m = list(map(int, input().split()))
lst = []
for i in m:
    if i not in lst:
        lst.append(i)
print(len(lst))