string = input()

vowells = ["a", "y", "i", "u", "e", "o"]

string1 = []

for i in string:
    if i.lower() not in vowells:
        string1.append(i.lower())

print("." + ".".join(string1))