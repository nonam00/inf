numbers = [int(x) for x in open('1.txt')]
counter = 0
mx = max(x for x in numbers if abs(x) % 10 == 3)
r = []
for i in range(len(numbers) - 1):
    if (abs(numbers[i]) % 10 == 3) + (abs(numbers[i + 1]) % 10 == 3) == 1:
        if numbers[i] ** 2 + numbers[i + 1] ** 2 >= mx ** 2:
            r.append(numbers[i] ** 2 + numbers[i + 1] ** 2)
print(len(r), max(r))

