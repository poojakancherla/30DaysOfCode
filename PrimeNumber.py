def isPrime(a):
    x = True
    if a == 1:
        print('Not prime')
    else:
        for i in range(2, int(a**0.5) + 1):
            if a % i == 0:
                x = False

    if x:
        print('Prime')
    else:
        print('Not Prime')


t = int(input())
for i in range(t):
    num = int(input())
    isPrime(num)
