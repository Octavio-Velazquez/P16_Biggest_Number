my_numbers = [28, 25, 142, 2, 27, 65, 99]

def getBiggest(numbers):
    """Obtain the biggest number from a list."""

    if len(numbers) == 0:
        return None

    biggest = numbers[0]
    for number in numbers:
        if number > biggest:
            biggest = number

    return biggest

print(getBiggest(my_numbers))

