arr = [3, 2, 1]
temp = ''
flag = 0
count = 0
for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            count += 1
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            flag = 1
    if flag == 0:
        break

print('Array is sorted in ' + str(count) + ' swaps')
print('First Element: ' + str(arr[0]))
print('Last Element: ' + str(arr[len(arr)-1]))
