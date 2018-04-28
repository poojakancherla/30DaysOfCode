
n = int(input())
d = dict(input().split() for _ in range(n))

for i in range(n):
    query = input()
    if query in d.keys():
        print(query + '=' + d[query])
    else:
        print("Not found")
