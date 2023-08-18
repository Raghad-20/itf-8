def find_smallest_and_largest(numbers):
    numbers.sort()
    smallest = numbers[0]
    largest = numbers[-1]
    return smallest, largest

def main():
    num_list = [12, 45, 6, 23, 1, 67, 9]
    smallest, largest = find_smallest_and_largest(num_list)
    print(f"The smallest number is: {smallest}")
    print(f"The largest number is: {largest}")


main()

