n, l = map(int, input().split())
lights = input().split()

lights = list(map(int, lights))

lights.sort()

differences = []
special_diff = [lights[0] - 0, l - lights[n-1]]

for i in range(n - 1):
    differences.append(lights[i+1] - lights[i])

if n == 1:
    differences.append(0)
if max(differences) / 2 > max(special_diff):
    result = max(differences) / 2
    print(f"{result:.10f}")
else:
    result = max(special_diff)
    print(f"{result:.10f}")