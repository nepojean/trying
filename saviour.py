from itertools import combinations

helper = ["G", "G", "B", "R", "G", "B", "B", "B", "B", "B", "R", "R", "R", "G"]
actual = [-1, -3, 4, -5, 7, 10, -8, 6, 7, 4, -3, 2, 9 , -4]

result = []

# generate all possible subsets within 1, 2, 3, 4, ... till len(actual)
# for each generated array, store tripple of the first one in result,
# then store tripple of the susequent ones if they do not contain the same thing inside helper.
# then leave the subsequent one if they contain the same letter within helper with the leftmost thing.

def generate_subsets():
    nums = [1,2,3,4,5,6,7,8,9,10,11, 12, 13, 14]
    subsets = []

    for r in range(len(nums) + 1):
        for combo in combinations(nums, r):
            subsets.append(list(combo))

    return subsets
all_combo = generate_subsets()



def choice(array):
    result = []
    length_array = len(array)
    for i in range(length_array):
    # tripple of the first selected.
        if i == 0:
            result.append(actual[array[0] - 1] * 3)
            # print(f"appending a tripple of {actual[array[0] - 1]}")
        if i > 0:
            # Tripple if the leftmost has a differnt color
            if helper[array[i] - 1] != helper[array[i - 1] -1]:
                result.append(actual[array[i] - 1] * 3)
                # print(f"appending a tripple of {actual[array[i] - 1]}")
            else:
                # Don't tripple if the left most has the same color
                result.append(actual[array[i] - 1])
                # print(f"appending just {actual[array[i] - 1]}")
    return result


totals = []

# for i in all_combo:
#     print(i)
# arrays = [[1, 2, 3], [2, 4]]
# for i in arrays:                     was a test dudette!
#     print(choice(i))
# print(totals)

for i in all_combo:
    sums = sum(choice(i))
    totals.append(sums)

print(max(totals))
