import os

EXIT = "EXIT"

accepted_products = ["milk", "chocolate", "eggs", "pen", "chicken"]


def add_product():
    product = None
    while product not in accepted_products:
        product = input("Enter a product ({} to close): ".format(EXIT))

        if product == EXIT:
            break

        if product not in accepted_products:
            os.system('cls')
            print("The product is out of stock")

    return product


# def write_file(filename, shopping_list):
#    file = open(f"{filename}.txt", "w")
#    file.write("\n".join(shopping_list))
#    file.close()
def write_file(filename, shopping_list):
    with open(f"{filename}.txt", "w") as file:
        file.write("\n".join(shopping_list))


def main():
    os.system('cls')
    shopping_list = []

    item = add_product()

    while item != EXIT:
        shopping_list.append(item)
        print("\n".join(shopping_list))
        item = add_product()
        os.system('cls')

    os.system('cls')

    if len(shopping_list) > 0:
        filename = input("Enter the file name: ")
        write_file(filename, shopping_list)


if __name__ == "__main__":
    main()
