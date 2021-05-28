from operator import itemgetter
import ast
import sys

current_word = None
current_count = 0
word = None
minconfidence = 5
addeditemtype = []
items = []
selected = []

for line in sys.stdin:
    datasubset = ast.literal_eval(line)
    for i in datasubset:
        if i[0] not in addeditemtype:
            addeditemtype.append(i[0])
            items.append(i)
        else:
            for j in items:
                if i[0] == j[0]:
                    j[1] = j[1] + i[1]

for i in items:
    if i[1] >= minconfidence:
        selected.append(i[0])

print(selected)
