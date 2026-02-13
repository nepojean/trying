the_sum = input()

array1 = []

for i in the_sum:
    if i != "+":
        array1.append(i)

array1.sort()

print("+".join(array1))
    