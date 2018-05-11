a = "pojasmayerxzqi"

l = []
s = ""

for i in range(len(a)):
    if a[i] not in s:
        s = s + a[i]
    else:
        l.append((len(s), s))
        last_occ = a.find(a[i],0, i)
        s = ""
        s = a[last_occ + 1 : i+1]
    l.append((len(s), s))


print(max(l)[1])
