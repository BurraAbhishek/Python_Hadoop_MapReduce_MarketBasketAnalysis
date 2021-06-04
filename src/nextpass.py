import json
import ast


def nextPass():
    """ Indicate next pass

    Add 1 to the pass attribute in the JSON file
    This module can run without Hadoop.
    """

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


def updateDiscarded():
    """ Update the list of discarded items from most recent pass """

    try:
        dfile = open("discarded_items.txt", "r")
        s1 = dfile.read()
        oldDiscarded = ast.literal_eval(s1)
        sfile = open("part-00000", "r")
        successAppend = 0
        while successAppend == 0:
            try:
                s2 = sfile.readline()
                # Remove unnecessary characters from list string.
                s2 = s2[0:-2]
                # Convert list into array
                addDiscarded = ast.literal_eval(s2)
                # Add the item to the full list of discarded items
                oldDiscarded.append(addDiscarded)
            except:
                successAppend = 1
                break
        wfile = open("discarded_items.txt", "w")
        wfile.write(str(oldDiscarded))
        wfile.close()
    except:
        # Print error message
        print("Couldn't update list of discarded items. Try manually.")

nextPass()
updateDiscarded()
