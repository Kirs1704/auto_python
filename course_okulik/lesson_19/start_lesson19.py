n = int(input())
s = [input().lower() for _ in range(n)]
for el in s:
    print(len(set(s)))


