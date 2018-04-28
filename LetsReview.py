n = int(input())
# for i in range(n):
#     s = input()
#     j = 0
#     while(j < len(s)):
#         print(s[j], end='')
#         j = j+2
#     print(" ", end = '')
#     j = 1
#     while(j < len(s)):
#         print(s[j], end = '')
#         j = j + 2
#     print()

# shorter method

for i in range(n):
    s = input()
    print(s[::2], s[1::2])
