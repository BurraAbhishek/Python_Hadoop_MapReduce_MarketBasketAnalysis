import json
import random


def rowcount():
    """ Returns the number of rows of the required dataset (type: integer) """

    try:
        # Prompt user for number of itemsets
        # Each itemset contains one or more items.
        rows = int(input("Number of itemsets (1 or more): "))
        # There should be at least one row.
        if rows < 1:
            # Condition violated: user should try again
            rows = rowcount()
    except:
        # Invalid input: user should try again
        rows = rowcount()
    return rows


def generate_dataset():
    """ Create a JSON dataset out of the JSON item list file """

    # Get the number of itemsets.
    rows = rowcount()
    try:
        # Get the item list from the item list file
        with open("items/item_list.json", "r") as itemjson:
            items = json.load(itemjson)
        # Get the total number of items in the item list.
        itemcount = len(items)
        # Create an array which will hold the dataset
        data = []
        # Each row of the dataset: Each sub-array
        for i in range(0, rows):
            # Add some random items to each sub-array from the list of items
            count = random.randint(1, itemcount)
            data_item = []
            for j in range(0, count):
                item_added = random.choice(items)
                data_item.append(item_added)
            data.append(data_item)
        # Save the dataset into the JSON file.
        jsonwrite = open("dataset/dataset.json", "w")
        json.dump(data, jsonwrite, indent=4)
        jsonwrite.close()
    except:
        print("Item list was not found")

generate_dataset()
