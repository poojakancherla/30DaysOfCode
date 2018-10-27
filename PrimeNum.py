def isPrime(a):
    if a == 2 or a == 3:
        print("Prime")
    elif a % 2 == 0 or a == 1:
        print('Not prime')
    else:
        x = all (a % i for i in range(2, int(a**0.5) + 1))
        if x:
            print('Prime')
        else:
            print('Not prime')

t = int(input())
for i in range(t):
    num = int(input())
    isPrime(num)
