n, t = map(int, input().split())
minutes = list(map(int, input().split()))

left = 0
current_sum = 0
book = 0

for right in range(n):
    current_sum += minutes[right]

    while current_sum > t:
        current_sum -= minutes[left]
        left += 1

    book = max(book, right - left + 1)

print(book)
