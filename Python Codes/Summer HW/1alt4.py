pairs = [[2, 5], [4, 2], [9, 8], [12, 10]]
count = 0

for pair in pairs:
    if all(num % 2 == 0 for num in pair):
        count += 1

print(count)