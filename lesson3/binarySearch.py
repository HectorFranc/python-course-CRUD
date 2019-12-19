import random


def binarySearch(data, target):
    data = sorted(data)
    min, max = 0, len(data) - 1

    while min <= max:
        actual_index = (min + max) // 2

        if target == data[actual_index]:
            return True
        elif target < data[actual_index]:
            max = actual_index - 1
        else:
            min = actual_index + 1
    return False


if __name__ == '__main__':
    random_numbers = [random.randint(0, 100) for i in range(20)]

    print(random_numbers)

    found = binarySearch(random_numbers, int(input('What number would you like to found? ')))

    print(found)
