def print_readings(readings):
    for i in range(len(readings)):
        if i > 0:
            print(" ", end="")
        print(readings[i], end="")
    print()


def count_above(readings, threshold):
    count = 0
    for reading in readings:
        if reading > threshold:
            count += 1
    return count


def remove_lowest(readings):
    if not readings:
        return
    lowest_index = 0
    for i in range(1, len(readings)):
        if readings[i] < readings[lowest_index]:
            lowest_index = i
    readings.pop(lowest_index)


def main():
    readings = []
    number = int(input("How many security readings were intercepted? "))
    for i in range(number):
        reading = int(input("Enter a security reading: "))
        readings.append(reading)
    threshold = int(input("Enter the threshold: "))
    print("Original security readings: ", end="")
    print_readings(readings)
    count = count_above(readings, threshold)
    print(f"Readings above {threshold}: {count}")
    remove_lowest(readings)
    print("After removing the lowest reading: ", end="")
    print_readings(readings)


if __name__ == "__main__":
    main()
