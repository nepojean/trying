string1 = input()
string2 = input()

if string1.lower() < string2.lower():
    print(-1)
if string1.lower() == string2.lower():
    print(0)
if string1.lower() > string2.lower():
    print(1)

