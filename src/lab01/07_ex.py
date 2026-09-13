s = input("in: ")
AL = 'QWERTYUIOPASDFGHJKLZXCVBNM'
k = ''
for i in range(len(s)):
    if s[i] in AL:
        s = s[i:]
        for i1 in range(len(s)):
            if i1 % 3 == 0:
                k += s[i1]

        break

print(f'out: {k}')