def total_of(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total


def largest_of(numbers):
    biggest = numbers[0]
    for number in numbers:
        if number > biggest:
            biggest = number
    return biggest


readings = [12, 7, 19, 3]

print(total_of(readings))
print(total_of([]))
print(largest_of(readings))
