arr1 = input ("Enter the number of contestants, and the benchmark: ")
arr2 = input ("Now enter the scores of all contestants: ")

int_arr1 = [int(i) for i in arr1.split()]
int_arr2 = [int(i) for i in arr2.split()]

counter = 0
benchmark = int_arr1[1]
for i in range(benchmark):
    if int_arr2[i] >= benchmark  and int_arr2[i] != 0:
        counter += 1

print(f"Number of passing individuals: {counter}")
