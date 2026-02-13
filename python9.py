import math
a, b = map(int, input().split())

i = 1

while pow(3, i) * a <= pow(2, i) * b:
    i += 1

print(i)