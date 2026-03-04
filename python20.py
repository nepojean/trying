n = int(input())

groups_size = list(input().split())

print(groups_size)


fours = []
threes = []
twos = []
ones = []

s_i = 0

for i in groups_size:
    if i == "4":
        fours.append(i)
    if i == "3":
        threes.append(i)
    if i == "2":
        twos.append(i)
    if i == "1":
        ones.append(i)



lenght_fours = len(fours)
lenght_threes = len(threes)
lenght_twos = len(twos)
lenght_ones = len(ones)

