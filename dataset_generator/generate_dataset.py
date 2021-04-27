import json
import random


def rowcount():
    try:
        rows = int(input("Number of items (1 or more): "))
        if rows < 1:
            rows = rowcount()
    except:
        rows = rowcount()
    return rows

def generate_dataset():
    rows = rowcount()
    try:
        with open("items/item_list.json", "r") as itemjson:
            items = json.load(itemjson)
        itemcount = len(items)
        data = []
        for i in range(0, rows):
            count = random.randint(1, itemcount)
            data_item = []
            for j in range(0, count):
                item_added = random.choice(items)
                data_item.append(item_added)
            data.append(data_item)
        jsonwrite = open("dataset/dataset.json", "w")
        json.dump(data, jsonwrite, indent=4)
        jsonwrite.close()
    except:
        print("Item list was not found")

generate_dataset()
