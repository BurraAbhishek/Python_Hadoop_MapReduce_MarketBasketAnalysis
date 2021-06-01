from operator import itemgetter
import ast
import sys
import json


def getMinConfidence():
    try:
        with open("apriori_settings.json", "r") as j:
            configs = json.load(j)
        minconfidence = configs["minimum-support"]
    except:
        # A reasonable user-defined value
        minconfidence = 5
    return minconfidence

current_word = None
current_count = 0
word = None
minconfidence = getMinConfidence()
addeditems = []
rejecteditems = []
items = []

for line in sys.stdin:
    # Convert input into list
    datasubset = ast.literal_eval(line)
    for i in datasubset:
        itemset = []
        for j in i:
            itemset.append(j[0])
        # Processing new itemset
        if itemset not in items:
            items.append(itemset)
            addeditems.append([itemset, 1])
        # Combining processed itemset.
        else:
            for j in range(0, len(items)):
                if items[j] == itemset:
                    addeditems[j][1] += 1


# Prepare to output list of discarded items
print("discarded" + '\t' + '[')

# Filter frequent item(sets)
for i in addeditems:
    if i[1] < minconfidence:
        print("frequent" + '\t' + str(i))
    else:
        print("discarded" + '\t' + str(i[0]) + ',')

# Complete the list of discarded items
print("discarded" + '\t' + ']')
