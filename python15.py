number = int(input())

array = []
for i in range(number):
    array.append(input().split())

test = [0, 0 , 0]
for i in array:
    test[0] += int(i[0])
    test[1] += int(i[1])
    test[2] += int(i[2])

if test == [0, 0 , 0]:
    print("YES")
else:
    print("NO")