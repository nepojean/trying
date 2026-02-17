num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 != 1 and num2 != 1 and num3 != 1:
    print(num1 * num2 * num3)
elif num1 == 1 and num2 > 1:
    print((num1 + num2) * num3)
elif num1 > num3 and num2 == 1:
    print(num1 * (num2 + num3))
elif num1 < num3 and num2 == 1:
    print((num1 + num2) * num3)
elif num3 == 1 and num2 > 1:
    print(num1 * (num2 + num3))