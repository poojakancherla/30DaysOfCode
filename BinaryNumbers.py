num = int(input())
s = []
counter = 0
maxones = 0
while(num > 1):
    s.append(int(num % 2))
    if int(num % 2) == 1:   counter = counter + 1
    else:   counter = 0
    maxones = max(counter, maxones)
    num = num / 2

print(maxones)
