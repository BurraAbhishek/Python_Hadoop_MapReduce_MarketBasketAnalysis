import sys
import itertools


def mapper():
    """ Emits k itemsets of the form <item, count> from a dataset """

    # Step 1: Generate the dataset
    for line in sys.stdin:
        line = line.strip()
        words = line.split(",")
        datasubset = []
        uniquedata = []
        for word in words:
            # Step 2: Map duplicates
            if word in uniquedata:
                for i in range(0, len(datasubset)):
                    if word == datasubset[i][0]:
                        datasubset[i][1] += 1
            else:
                datasubset.append([word, 1])
                uniquedata.append(word)
        # Step 3: Sort the dataset to avoid duplicated keys
        datasubset.sort()
    # Dataset is created as an input to reducer
        print(datasubset)

# First job only! For subsequent jobs use mapper.py
mapper()

