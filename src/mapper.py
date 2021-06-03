import sys
import itertools
import ast
import json


def getDiscardedItems():
    """ Get the list of discarded items """

    try:
        f = open("discarded_items.txt", "r")
        s = f.read()
        f.close()
        discarded = ast.literal_eval(s)
    except:
        discarded = []
    return discarded


def checkIfSubset(l, s):
    """ Check if list s is a subset of nested list l """

    result = False
    for i in s:
        if set(i).issubset(set(l)):
            result = True
    return result


def getItemsetLength():
    """ Get the length of each itemset combination """

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

    # Step 1: Get list of discarded items
    discarded = getDiscardedItems()
    # Step 2: Generate a stream of transactions from the CSV dataset
    for line in sys.stdin:
        line = line.strip()
        words = line.split(",")
        datasubset = []
        for word in words:
            # Step 3: Remove duplicates and empty words
            if word not in datasubset and len(word) > 0:
                datasubset.append(word)
        # Step 4: Sort the dataset to avoid duplicated keys
        datasubset.sort()
        # Step 5: Combine the items within a single transaction
        if len(datasubset) > 0:
            finaldatasubset = list(itertools.combinations(datasubset, n))
        # Dataset is created as an input to reducer and passed sequentially
        if len(finaldatasubset) > 0:
            # Print all key-value pair combinations not discarded
            for i in finaldatasubset:
                if len(i) > 0 and not IsSubset(i, discarded):
                    # To avoid problems in reducer, tab delimiter not used
                    print([i, 1])

# Running the mapper code
mapper(getItemsetLength())
