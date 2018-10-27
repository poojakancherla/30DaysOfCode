import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    l = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if emailID[-9:] == 'gmail.com':
            l.append(firstName)

sorted_l = sorted(l)

for i in sorted_l:
    print(i)
