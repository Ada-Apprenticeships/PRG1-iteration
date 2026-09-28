def countdown(start):
    count = start
    while count > 0:
        print(count)
        count = count - 1
    print("Liftoff")


def first_over(limit, readings):
    for reading in readings:
        if reading > limit:
            return reading
    return None


countdown(3)
countdown(0)

print(first_over(100, [45, 92, 130, 88]))
print(first_over(100, [45, 92, 88]))
