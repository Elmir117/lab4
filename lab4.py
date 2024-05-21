numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


with open('all_numbers.txt', 'w') as file:
    for number in numbers:
        file.write(f"{number}\n")


divisible_by_3 = []
with open('all_numbers.txt', 'r') as file:
    for line in file:
        number = int(line.strip())
        if number % 3 == 0:
            divisible_by_3.append(number)

with open('divisible_by_3.txt', 'w') as file:
    total = 0
    for number in divisible_by_3:
        file.write(f"{number}\n")
        total += number
    file.write(f"Total: {total}\n")

print(f"3-ə bölünən ədədlərin cəmi: {total}")
