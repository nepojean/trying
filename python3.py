import math
dictionary = {}
for i in range(5):
    dictionary[i] = input()

row = 0
column = 0
model = '0 0 0 0 0'

for i in range(5):
    if dictionary[i] != model:
        row = i + 1

helper = dictionary[row - 1].split()

counter = 0

while helper[counter] != '1':
    counter += 1

column = counter + 1

row_movements = abs(3 - row)
col_movements = abs(3 - column)

print(row_movements + col_movements)