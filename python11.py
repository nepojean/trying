k, n, w = map(int, input().split())

total_money = k * (1 + w) * w /2

if total_money > n:
    print(int(total_money - n))
else:
    print(0)