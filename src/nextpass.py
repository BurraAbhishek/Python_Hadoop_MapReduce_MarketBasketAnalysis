import json

# Indicate next pass
# Add 1 to the pass attribute in the JSON file
# This module can run without Hadoop.
try:
    # Load the JSON settings file
    with open("apriori_settings.json", "r") as j:
        configs = json.load(j)
    # Increment the pass attribute by 1
    configs["itemset-length"] += 1
    # Save the updated settings
    f = open("apriori_settings.json", "w")
    json.dump(configs, f, indent=4)
    f.close()
except:
    # Print error message
    print("Couldn't go to next pass")
