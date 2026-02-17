number = input()

length = len(number)

def permutations(array):
    array1 = [i + "4" for i in array]
    array2 = [i + "7" for i in array]

    array3 = array + array1 + array2
    return(list(set(array3)))


#check if it is lucky
#check if it is almost lucky
#otherwise it is unlicky "NO"



all_num = ["4", "7"]
for i in range(length - 1):
    all_num = permutations(all_num)

all_num_int = map(int, all_num)


# check if it is really a lucky number, then print YES.
checker = 0
for i in number:
    for j in i:
        if j != "4" and j != "7":
            checker += 1
if checker == 0:
    print("YES")
elif checker != 0:
    checker = 0
    for i in all_num_int:
        if int(number) % i == 0:
            checker += 1
    if checker != 0:
        print("YES")
    else:
        print("NO")
