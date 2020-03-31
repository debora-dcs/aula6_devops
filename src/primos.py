counter = 1
number = 2

while (counter < 100):
    regular = False
    for i in range(2, number):
        if (number % i == 0):
            regular = True
            break
    if (not regular):
        counter += 1
        print(number, end=' | ')

    number += 1

