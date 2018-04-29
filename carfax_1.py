s = input()
arr = s.split(", ")
for i in arr:
    print(i)
print()

arr = sorted(arr)
for i in arr:
    print(i)
print()

for i in range(len(arr) - 2):
    if arr[i] == arr[i+1]:
        del arr[i]
for i in arr:
    print(i)
print()

for i in arr:
    print(len(i))
