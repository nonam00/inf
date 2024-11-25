numbers = [int(x) for x in open('2.txt')]
mn = min(numbers)
r = []
for i in range(len(numbers) - 1):
    if numbers[i] % 35 == mn or numbers[i + 1] % 55 == mn:
        r.append(numbers[i] + numbers[i + 1])
print(len(r), min(r))
