import sys
import itertools


def mapper(n):
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
        # Step 4: Combine the items within a single transaction
        if len(datasubset) > 0:
            finaldatasubset = list(itertools.combinations(datasubset, n))
        # Dataset is created as an input to reducer and passed sequentially
        if len(finaldatasubset) > 0:
            # Print all the key-value pair combinations
            print(finaldatasubset)

# Test case
mapper(2)
