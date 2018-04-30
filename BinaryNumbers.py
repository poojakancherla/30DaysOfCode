num = int(input())
s = []
counter = 0
ones = 0
while(num > 1):
    s.append(int(num % 2))
    if int(num % 2) == 1:   counter = counter + 1
    else:   counter = 0
    ones = max(counter, ones)
    num = num / 2

print(ones)
