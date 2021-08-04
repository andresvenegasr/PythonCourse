def largest_string(*strings):
    largest = ""
    for string in strings:
        if len(string) > len(largest):
            largest = string
    return largest


def sum_list(numbers):
    accumulate = 0
    for number in numbers:
        accumulate += number
    return accumulate


def is_not_even_number(number):
    return number % 2 > 0


def main():
    print(largest_string("hello", "how", "are", "you", "today"))
    print(sum_list([1, 2, 3, 4, 5]))
    print(is_not_even_number(3))
    print(is_not_even_number(24))


if __name__ == "__main__":
    main()
