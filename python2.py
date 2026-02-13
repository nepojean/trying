import math
arr1 = input()

m, n = map(int, arr1.split())

area = m * n
max_domino = math.floor(area/2)
print(max_domino)