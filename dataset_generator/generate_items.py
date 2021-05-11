import json


def initialize_json():
    """ Create the item list file if it doesn't exist. """

    try:
        with open("items/item_list.json", "r") as itemjson:
            items = json.load(itemjson)
    except:
        # Create the item list
        jsondata = {"items": []}
        # Save the item list to the item list file
        jsonwrite = open("items/item_list.json", "w")
        json.dump(jsondata, jsonwrite, indent=4)
        jsonwrite.close()


def list_items():
    """ Display the list of items in the item list. """

    try:
        # Load the item list from the item list file
        with open("items/item_list.json", "r") as itemjson:
            items = json.load(itemjson)
            # Print each item from the list
            for i in items:
                print(i)
    except:
        print("The list was not created. ")


def add_items():
    """ Add an item to the item list. """

    # Load the item list from the item list file
    with open("items/item_list.json", "r") as itemjson:
        data = json.load(itemjson)
        # Prompt the user to add an item (Returns a string)
        new_item = input("Which item do you want to insert?")
        # Add the item to the item list
        data.append(new_item)
        # Save the new list to the item list file
        jsonwrite = open("items/item_list.json", "w")
        json.dump(data, jsonwrite, indent=4)
        jsonwrite.close()

initialize_json()
list_items()
add_items()
print("New itemset: ")
list_items()
