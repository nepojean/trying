import math
n = int(input())
sticks = list(map(int, input().split()))

# sum = 0
# for i in range(n):
#     sum += sticks[i]

# average = sum / n

low = min(sticks)
high = max(sticks)

diff_keeper = []

for i in sticks:
    sum = 0
    for j in range(low, high + 1):
        sum += abs(j - i)
    diff_keeper.append(sum)

print(diff_keeper)
