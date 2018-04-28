
n = int(input())
d = dict(input().split() for _ in range(n))

for i in range(n):

    try:
        query = input()
        print(query + '=' + d[query])

    except:
        print("Not found")
