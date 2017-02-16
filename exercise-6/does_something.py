import sys 
ebirdfile = open(sys.argv[1], encoding = "ISO-8859.15")
ebirddict = {}
ebirdfile.readline()
for row in ebirdfile:
    split = row.split(",")
    ebirddict[split[3]]=split[7]
for birdspecies in ebirddict:
    print("Species " + birdspecies + " is in the family " + ebirddict[birdspecies])
from collections import Counter
countebirds = Counter(ebirddict.values())
for key, value in countebirds.items():
    print("The family " + str(key) + " has " + str(value) + " total species.")
