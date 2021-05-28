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
items = []
selected = []

for line in sys.stdin:
    datasubset = ast.literal_eval(line)
    for i in datasubset:
        itemset = []
        for j in i:
            itemset.append(j[0])
        if itemset not in items:
            items.append(itemset)
            addeditems.append(i)
        else:
            for j in range(0, len(items)):
                if items[j] == itemset:
                    for k in range(0, len(i)):
                        addeditems[j][k][1] += i[k][1]

for i in addeditems:
    isSelected = True
    for j in i:
        if j[1] < minconfidence:
            isSelected = False
    if isSelected:
        print(i)
