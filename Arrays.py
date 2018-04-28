size = int(input())
arr = list(int(x) for x in input().split())
arr = [str(x) for x in arr]
print(" ".join(arr[::-1]))
