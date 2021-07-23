import os

# Welcome message
print('Welcome to the Shopping list')
input('Press any key to continue...')
os.system('cls')

# Define the accepted options
options = ['A', 'S', 'Q']
selected_option = None

# Define variable to determine if the program must closed
exit_list = False

# Define variable to store de products
shopping_list_items = []

while not exit_list:

    # Request option to choose
    while selected_option not in options:
        selected_option = input('Select an option [A]dd, [S]how, [Q]uit: ')
        os.system('cls')

    # Code for add item process
    if selected_option == 'A':
        item = input('Enter the product: ')
        os.system('cls')

        # If the element is in the list shows a message.
        if item in shopping_list_items:
            print('The product is already in the list.')
            input('Press any key to continue...')

        # Add the product in the list
        else:

            # Add confirmation to add the product
            confirmation = None
            while confirmation not in ['Y', 'N']:
                confirmation = input('Are you sure that you want to add this element? [Y/N]')

            # If the confirmation is Y the product will be added to the list
            if confirmation == 'Y':
                shopping_list_items.append(item)
                print(f'The {item} item was added successfully')
            else:
                print(f'The {item} item was not added to the list')

            input('Press any key to continue...')

    # Code for Show option process
    elif selected_option == 'S':

        # Validate if the list has items
        if len(shopping_list_items) > 0:
            legend = 'The elements in the list are: '
            print(legend)
            print('{}'.format('-' * len(legend)))

            for items in shopping_list_items:
                print(f'----> {items}')

            input('Press any key to continue...')

        # If the list is empty shows a message.
        else:
            print('The list is empty.')
            input('Press any key to continue...')

    elif selected_option == 'Q':
        exit_list = True

        legend = 'The elements in the list are: '
        print(legend)
        print('{}'.format('-' * len(legend)))

        for items in shopping_list_items:
            print(f'----> {items}')

        print('{}'.format('-' * len(legend)))

        print('Goodby!!! :)')
        input('Press any key to continue...')
    else:
        print("Invalid option")

    selected_option = None
    os.system('cls')
