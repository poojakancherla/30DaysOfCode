s = "aaaaabirrrtuuuupo"
counter = 0
max_length = (0, "")
last_seen = ""
for i in range(len(s)):    
    if s[i] == last_seen:
        counter = counter + 1

    else:
        if counter > max_length[0]:
            max_length = (counter, last_seen)
        last_seen = s[i]
        counter = 1
print(max_length)
