def get_length(iterable, *args):
    if args:
        length = [len(iterable)]
        for item in args:
            length.append(len(item))
        return length
    return len(iterable)


def main():
    print(get_length("Hello"))
    print(get_length("Hello", "How", "are", "you"))


if __name__ == "__main__":
    main()
