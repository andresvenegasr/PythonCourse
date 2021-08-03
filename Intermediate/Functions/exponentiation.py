def exponentiation(number, potency=0):
    if potency == 0:
        return pow(number, 2)
    return pow(number, potency)


def main():
    print(exponentiation(2))
    print(exponentiation(3))
    print(exponentiation(3, 3))
    print(exponentiation(3, 9))


if __name__ == "__main__":
    main()
