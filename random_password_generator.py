# generates the random password from selected amounts of the letters, numbers and symbols.
# No AI used.

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
result = ""
total = nr_letters + nr_symbols + nr_numbers
i_letters = nr_letters
i_symbols = nr_symbols
i_numbers = nr_numbers


for s in range(1, total + 1):
    rand_total = 0
    if i_letters > 0:
        rand_total += 1
    if i_numbers > 0:
        rand_total += 1
    if i_symbols > 0:
        rand_total += 1

    rand_number = random.randint(1, rand_total)


    if rand_number == 1 and rand_total == 3:
        result = result + letters[random.randint(0, len(letters) - 1)]
        i_letters -= 1

    if rand_number == 2 and rand_total == 3:
        result = result + numbers[random.randint(0, len(numbers) - 1)]
        i_numbers -= 1

    if rand_number == 3 and rand_total == 3:
        result = result + symbols[random.randint(0, len(symbols) - 1)]
        i_symbols -= 1



    if rand_number == 1 and rand_total == 2:
        if i_letters > 0:
            result = result + letters[random.randint(0, len(letters) - 1)]
            i_letters -= 1
        elif i_numbers > 0:
            result = result + numbers[random.randint(0, len(numbers) - 1)]
            i_numbers -= 1
        elif i_symbols > 0:
            result = result + symbols[random.randint(0, len(symbols) - 1)]
            i_symbols -= 1


    if rand_number == 2 and rand_total == 2:
        if i_numbers > 0:
            result = result + numbers[random.randint(0, len(numbers) - 1)]
            i_numbers -= 1
        elif i_symbols > 0:
            result = result + symbols[random.randint(0, len(symbols) - 1)]
            i_symbols -= 1
        elif i_letters > 0:
            result = result + letters[random.randint(0, len(letters) - 1)]
            i_letters -= 1


    if rand_total == 1:
        if i_symbols > 0:
            result = result + symbols[random.randint(0, len(symbols) - 1)]
            i_symbols -= 1
        elif i_letters > 0:
            result = result + letters[random.randint(0, len(letters) - 1)]
            i_letters -= 1
        elif i_numbers > 0:
            result = result + numbers[random.randint(0, len(numbers) - 1)]
            i_numbers -= 1

print(result)
