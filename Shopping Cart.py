# a shopping cart is a list of items, we then add

import os

shopping_list = []

# clear screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# add_items
def add_to_list(item):
    shopping_list.append(new_item)
    print("Added! list has {} items".format(len(shopping_list)))
# show_contents
def show_list():
    clear_screen()
    print("here is your shopping_list")
    for item in shopping_list:
        print(item)


# help
def show_help():
    print("What should you pick up at store")
    print('''
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for help
    Enter 'SHOW to see the current list
    ''')

show_help()

# iteration

while True:
    new_item = input(" > ")

    if new_item == 'DONE':
        break
    if new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue

    add_to_list(new_item)