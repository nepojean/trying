l = 9
string = "11011"

def permutations(array):
    array1 = [i + "0" for i in array]
    array2 = [i + "1" for i in array]

    array3 = array + array1 + array2
    return(list(set(array3)))


all_strings = ["1", "0"]
for i in range(10):
    all_strings = permutations(all_strings)

needed = []
for i in all_strings:
    if len(i) == 11:
        needed.append(i)

result = list(set(needed))

def check_sim(str):
    for i in range(0, len(str) + 1):
        if i < 4:
            if str[i:i + 5] == "11011":
                return 1
        if i >= 4:
            if str[i - 5:i] == "11011":
                return 1

counter  = 0
for i in result:
    if check_sim(i):
        counter += 1

print(counter)