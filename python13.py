word = input()
lowers = 0
uppers = 0
for i in word:
    if i.islower():
        lowers += 1
    if i.isupper():
        uppers += 1

if uppers == lowers:
    print(''.join(word).lower())
if uppers > lowers:
    print(''.join(word).upper())
if uppers < lowers:
    print(''.join(word).lower())