import json


def initialize_json():
    try:
        with open("items/item_list.json", "r") as itemjson:
            items = json.load(itemjson)
    except:
        jsondata = {"items": []}
        jsonwrite = open("items/item_list.json", "w")
        json.dump(jsondata, jsonwrite, indent=4)
        jsonwrite.close()

def list_items():
    try:
        with open("items/item_list.json", "r") as itemjson:
            items = json.load(itemjson)
            for i in items:
                print(i)
    except:
        print("The list was not created. ")

def add_items():
    with open("items/item_list.json", "r") as itemjson:
        data = json.load(itemjson)
        new_item = input("Which item do you want to insert?")
        data.append(new_item)
        jsonwrite = open("items/item_list.json", "w")
        json.dump(data, jsonwrite, indent=4)
        jsonwrite.close()        

initialize_json()
list_items()
add_items()
print("New itemset: ")
list_items()
    
    
