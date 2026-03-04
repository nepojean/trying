n, m = map(int, input().split())

friendships = []

for i in range(m):
    friendships.append(input().split())

if int((m-1) * (m) * 0.5) == m:
    print("IMPOSSIBLE")


