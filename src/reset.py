import json

# Reset all settings
try:
    # Load the JSON settings file
    with open("apriori_settings.json", "r") as j:
        configs = json.load(j)
    # Reset the pass attribute to 1
    configs["itemset-length"] = 1
    # Save the updated settings
    f = open("apriori_settings.json", "w")
    json.dump(configs, f, indent=4)
    f.close()
    # Reset the list of discarded items to an empty list.
    o = open("discarded_items.txt", "w")
    o.write("[]")
    o.close()
except:
    # Print error message
    print("Couldn't reset the program.")
