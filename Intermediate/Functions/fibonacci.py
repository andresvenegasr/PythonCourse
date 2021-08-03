def fibonacci_sequence(limit):
    if limit == 0 or limit == 1:
        return 1
    else:
        return fibonacci_sequence(limit - 1) + fibonacci_sequence(limit - 2)


def main():
    print("Fibonacci sequence")
    limit = int(input("Enter a number of the sequence: "))
    print(fibonacci_sequence(limit))


if __name__ == "__main__":
    main()
