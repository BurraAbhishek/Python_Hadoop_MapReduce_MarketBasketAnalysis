import sys
import itertools
import json


def getItemsetLength():
    try:
        with open("apriori_settings.json", "r") as j:
            configs = json.load(j)
        setlength = configs["itemset-length"]
    except:
        # Use pairs if no permitted value
        setlength = 2
    return setlength


def mapper(n):
    """ Emits k itemsets of the form <item, count> from a dataset """

    # Step 1: Generate the dataset
    for line in sys.stdin:
        line = line.strip()
        words = line.split(",")
        datasubset = []
        uniquedata = []
        for word in words:
            # Step 2: Remove duplicates
            if word not in uniquedata:
                datasubset.append([word, 1])
                uniquedata.append(word)
        # Step 3: Sort the dataset to avoid duplicated keys
        datasubset.sort()
        # Step 4: Combine the items within a single transaction
        if len(datasubset) > 0:
            finaldatasubset = list(itertools.combinations(datasubset, n))
        # Dataset is created as an input to reducer and passed sequentially
        if len(finaldatasubset) > 0:
            # Print all the key-value pair combinations
            print(finaldatasubset)

# Running the mapper code
mapper(getItemsetLength())
