import math
distance = input()

if int(distance) % 5 == 0:
    act_distance = math.floor(int(distance) / 5)
else:
    act_distance = math.floor(int(distance) / 5 + 1)

print(act_distance)