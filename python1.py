arr1 = input ()
arr2 = input ()

int_arr1 = [int(i) for i in arr1.split()]
int_arr2 = [int(i) for i in arr2.split()]

counter = 0
benchmark = int_arr1[1]
length = int_arr1[0]
for i in range(length):
    if int_arr2[i] >= int_arr2[benchmark - 1]  and int_arr2[i] != 0:
        counter += 1

print(counter)
