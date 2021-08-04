import os

EXIT = "EXIT"
FILENAME = "shopping_list.txt"

accepted_products = ["milk", "chocolate", "eggs", "pen", "chicken"]


def add_product():
    product = ""
    while product.lower() not in accepted_products and product != EXIT:
        product = input("Enter a product ({} to close): ".format(EXIT))

        if product not in accepted_products:
            os.system('cls')
            print("The product is out of stock")

    return product


# def write_file(filename, shopping_list):
#    file = open(f"{filename}.txt", "w")
#    file.write("\n".join(shopping_list))
#    file.close()
def write_file(shopping_list):
    with open(FILENAME, "w") as file:
        file.write("\n".join(shopping_list))


def open_file():
    if input("Do you want open the file to load the list? [y/n] ") == "y":
        try:
            with open(FILENAME, "r") as file:
                return file.read().split("\n")
        except FileNotFoundError:
            print(f"The file {FILENAME} does not exists.")
            return []
    else:
        return []


def main():
    os.system('cls')
    shopping_list = open_file()

    item = add_product()

    while item != EXIT:

        if item.lower() in [_item.lower() for _item in shopping_list]:
            print("The product already exists")
        else:
            shopping_list.append(item)

        print("\n".join(shopping_list))
        item = add_product()
        os.system('cls')

    os.system('cls')

    if len(shopping_list) > 0:
        write_file(shopping_list)


if __name__ == "__main__":
    main()
